'''
Created on 04/04/2013
Updated 26/08/2015 - Protocol V1.1 examples

@author: Tim Warren / Saturn South
Very simple demonstration of a lightweight ESCo in Python Twisted

'''

from twisted.internet import reactor
from twisted.web import server, resource
from influxdb import InfluxDBClient 
from datetime import datetime
import time
import cred as cred
import SSMessages_8834 as M
import json
import numpy as np
import pandas as pd
import requests

SERVER_PORT = 8081


#---------------------------------------------------------------------------# 
# setup influxdb client
#---------------------------------------------------------------------------# 



influx_client = InfluxDBClient('cred.IP', '8086', 'cred.USER', 'cred.PWD', 'cred.DB')
#influx_client = DataFrameClient('IP', 'port', 'USER', 'PWD', 'DB')

PROTOCOL_VERSION = "1.1"
VOLTAGE_ATTR_ID = 57610

VOLTAGE_ATTR_DIVISOR = 100

def generate_container(messages):
    new_container = {}
    new_container[M.F.Gen.ProtocolVersion_1_1] = PROTOCOL_VERSION
    new_container[M.F.Gen.Messages_1_1] = messages
    return new_container

def generate_close_connection():
    new_message = {}
    new_message[M.F.Gen.Cluster_1_1] = M.Clusters_1_1.SS_ESB
    new_message[M.F.Gen.MsgID_1_1] = M.SS_ESB.E.CloseConnection_1_1
    return new_message

def generate_get_latest_readings():
    new_message = {}
    new_message[M.F.Gen.Cluster_1_1] = M.Clusters_1_1.SS_ESB
    new_message[M.F.Gen.MsgID_1_1] = M.SS_ESB.E.GetData_1_1
    new_message[M.F.Dat.Source] = M.V.Dat.Source.LatestReadings_1_1
    return new_message

def toggle_relay():
    new_message = {}
    new_message[M.F.Gen.Cluster_1_1] = M.Clusters_1_1.OnOff
    new_message[M.F.Gen.MsgID_1_1] = M.OnOff.E.SwitchState
    new_message[M.F.Nwk.DevIEEE]="001BC502B0102AA3"
    new_message[M.F.Nwk.EndpointID]=1
    new_message[M.F.OnOff.Action]=M.V.OnOff.Toggle
    return new_message

def process_data(json_data):
    # Very basic (and silly) data parser to stoke the fires of industry
    
    # First sort the wrapper based on the protocol version
    if M.F.Gen.ProtocolVersion in json_data:
        if json_data[M.F.Gen.ProtocolVersion] == "1.0":
            process_protocol_1_0(json_data)
        else:
            print "Invalid or unknown protocol version from ESBox: %s" % json_data[M.F.Gen.ProtocolVersion]
    elif M.F.Gen.ProtocolVersion_1_1 in json_data:
        if json_data[M.F.Gen.ProtocolVersion_1_1] == "1.1":
            #process_protocol_1_1(json_data)
            process_db(json_data)
        else:
            print "Invalid or unknown protocol version from ESBox: %s" % json_data[M.F.Gen.ProtocolVersion_1_1]
    else:
        print "Malformed ESBox message wrapper received (no protocol version)"
        
def process_protocol_1_0(json_data):
    if M.F.Gen.ESBoxVersion in json_data:
        if M.F.Gen.Messages in json_data:
            for each_message in json_data[M.F.Gen.Messages]:
                if each_message[M.F.Gen.MsgID] == M.SS_ESB.E.NoFurtherMessages:
                    print "\tNo further messages."
                    continue
                print "Received an unrecognised V1.0 message from the ESBox: %s" % json_data
        else:
            # Got a message we don't recognise
            print "Received an invalid V1.0 message from the ESBox: %s" % json_data
        
def process_protocol_1_2(json_data):        
    if M.F.Gen.ESBoxVersion_1_1 in json_data:
        print(json_data)

    else:
            # Got a message we don't recognise
        print "Received an invalid V1.1 message from the ESBox: %s" % json_data
            
def process_protocol_1_1(json_data):        
    if M.F.Gen.ESBoxVersion_1_1 in json_data:
        if M.F.Gen.Messages_1_1 in json_data:
            for each_message in json_data[M.F.Gen.Messages_1_1]:
                if each_message[M.F.Gen.MsgID_1_1] == M.SS_ESB.E.NoFurtherMessages_1_1:
                    continue
                if (each_message[M.F.Gen.MsgID_1_1] == M.SS_ESB.E.SendData):
                    if each_message[M.F.Dat.Source] == M.V.Dat.Source.LatestReadings_1_1:
                        for each_han_endpoint in each_message[M.F.Dat.Data_1_1]:
                            
                            this_node_ieee = each_han_endpoint[M.F.Nwk.HAN_1_1]
                            this_endpoint_id = each_han_endpoint[M.F.Nwk.EndpointID_1_1]
                           
                            for each_cluster in each_han_endpoint[M.F.Dat.Clusters_1_1]:
                                if each_cluster[M.F.Gen.Cluster_1_1] == M.Clusters_1_1.SM:  # Is this data from the simple metering cluster?
                                    for each_attr in each_cluster[M.F.Dat.Attributes_1_1]:                                   
                                        if each_attr[M.F.Dat.AttributeID_1_1] == VOLTAGE_ATTR_ID:
                                            continue
                                        #if each_attr[M.F.Dat.AttributeID_1_1] == CURRENT_ATTR_ID:
                                        #    print "\t\t %s  " % (this_node_ieee) + str(float(each_attr[M.F.Dat.Data_1_1])/CURRENT_ATTR_DIVISOR)
                    continue   
                print "Received an unrecognised V1.1 message from the ESBox: %s" % json_data
        else:
            print "Received an invalid V1.1 message from the ESBox: %s" % json_data

def process_db(json_data):
    read_time = datetime.utcnow()
    if M.F.Gen.ESBoxVersion_1_1 in json_data:
        if M.F.Gen.Messages_1_1 in json_data:
            for each_message in json_data[M.F.Gen.Messages_1_1]:
                if each_message[M.F.Gen.MsgID_1_1] == M.SS_ESB.E.NoFurtherMessages_1_1:
                    continue
                if (each_message[M.F.Gen.MsgID_1_1] == M.SS_ESB.E.SendData):
                    if each_message[M.F.Dat.Source] == M.V.Dat.Source.LatestReadings_1_1:
                        for each_han_endpoint in each_message[M.F.Dat.Data_1_1]:
                            this_node_ieee = each_han_endpoint[M.F.Nwk.HAN_1_1]
                            for each_cluster in each_han_endpoint[M.F.Dat.Clusters_1_1]:
                                if each_cluster[M.F.Gen.Cluster_1_1] == M.Clusters_1_1.SM:  # Is this data from the simple metering cluster?
                                    for each_attr in each_cluster[M.F.Dat.Attributes_1_1]:

                                        send_points = [
                                            {
                                                "measurement": "readings",
                                                "tags": {
                                                    "ieee": str(each_han_endpoint[M.F.Nwk.HAN_1_1]),
                                                },
                                                "time": int(time.time()),
                                                "fields": {
                                                    "ieee": str(each_han_endpoint[M.F.Nwk.HAN_1_1]),
                                                    str(each_attr[M.F.Dat.AttributeID_1_1]): int(each_attr[M.F.Dat.Data_1_1])
                                                }
                                            }
                                        ]
                                        
                                        
                                        influx_client.write_points(send_points, time_precision='s')
                                        print "reading submited"
                    continue   
                print
        else:
            print




class TestServer(resource.Resource):
    isLeaf = True
    
    num_get_requests = 0
    time_of_last_readings = time.time()-10
    
    def render_GET(self, request):
        #self.numberGETRequests += 1
        request.setHeader("content-type", "text/plain")
        print "Have been visited by a web browser " + str(self.num_get_requests) + " times!"
        return "Hello there! You're not an ESBox!\n"
    
    def render_PUT(self, request):
        
       # print "\n"
        
        # Read the content of the PUT request
        data = request.content.read()
        
        # We'll try to decode JSON sent by the ESBox here
        try:
            decoded_json = json.loads(data)            
            # Send it elsewhere for processing          
        except:
          #  print "Couldn't decode valid JSON from the ESBox message wrapper :("
            return
         
        process_data(decoded_json)
     
        # Prepare the response message and container for the ESBox
        request.setHeader("content-type", "application/json")
        
        # For now we're just going to see if it's been more than 10 seconds since we last requested latest readings, and if so we'll send a 
        # GetData message and ask for the latest readings. Otherwise, we'll just close the connection.
        if time.time() - self.time_of_last_readings > 10:
#            print "Requesting latest readings."
            response_message = generate_get_latest_readings()
            #print "Toggle device relay."
            #esponse_message = toggle_relay()
            self.time_of_last_readings = time.time()
        else:
#            print "Closing connection to ESBox."
            response_message = generate_close_connection()
        response_container = generate_container( [response_message] )
        
        return json.dumps(response_container)




    
reactor.listenTCP(SERVER_PORT, server.Site(TestServer()))
reactor.run()
