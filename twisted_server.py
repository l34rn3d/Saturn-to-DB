'''
Created on 04/04/2013
Updated 26/08/2015 - Protocol V1.1 examples

@author: Tim Warren / Saturn South
Very simple demonstration of a lightweight ESCo in Python Twisted

Runs on Python 2.7.3 and Twisted 13
'''
#********************************************************************
#
#                      Software License Agreement
#
# The software supplied herewith by Saturn South Pty Ltd (the
# "Company") for its Saturn Energy products is intended and supplied
# to you, the Company's customer, for use soley and exclusively
# with Saturn Energy products.
#
# You may not use, inspect, view, reverse engineer, modify or
# distribute the software without prior express written permission
# from the Company.
#
# The software is considered 'confidential information'.
#
# The software is owned by the Company and/or its supplier, and is
# protected under applicable copyright laws. All rights are
# reserved. Any use in violation of the foregoing restrictions may
# subject the user to criminal sanctions under applicable laws, as
# well as to civil liability for the breach of the terms and
# conditions of this license.
#
# THIS SOFTWARE IS PROVIDED IN AN "AS IS" CONDITION. NO WARRANTIES,
# WHETHER EXPRESS, IMPLIED OR STATUTORY, INCLUDING, BUT NOT LIMITED
# TO, IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE APPLY TO THIS SOFTWARE. THE COMPANY SHALL NOT,
# IN ANY CIRCUMSTANCES, BE LIABLE FOR SPECIAL, INCIDENTAL OR
# CONSEQUENTIAL DAMAGES, FOR ANY REASON WHATSOEVER.
#
#*******************************************************************

from twisted.internet import reactor
from twisted.web import server, resource
import SSMessages_8834 as M
import json
import time

SERVER_PORT = 8081

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
    new_message[M.F.Nwk.DevIEEE]="001BC502B0102974"
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
            process_protocol_1_1(json_data)
        else:
            print "Invalid or unknown protocol version from ESBox: %s" % json_data[M.F.Gen.ProtocolVersion_1_1]
    else:
        print "Malformed ESBox message wrapper received (no protocol version)"
        
def process_protocol_1_0(json_data):
    if M.F.Gen.ESBoxVersion in json_data:
        print "[1.0] ESBox with version " + json_data[M.F.Gen.ESBoxVersion] + " sent some data."
        
        if M.F.Gen.Messages in json_data:
            # Here is where we parse V1.0 protocol messages
            for each_message in json_data[M.F.Gen.Messages]:
                # Check for a 'no further messages' message
                if each_message[M.F.Gen.MsgID] == M.SS_ESB.E.NoFurtherMessages:
                    print "\tNo further messages."
                    continue
                
                # Un-comment the following section if you want to be able to process V1.0 SendLatestReadings messages (you shouldn't need to do this unless using pre-8834 ESBox releases)
                '''
                if (each_message[M.F.Gen.MsgID] == M.SS_ESB.E.SendLatestReadings and    # Check for latest readings report
                    each_message[M.F.Gen.Cluster] == M.Clusters.SS_ESB):                 # from the correct cluster
                    
                    for each_endpoint in each_message[M.F.Nwk.Endpoints]:
                        
                        this_node_ieee = each_endpoint[M.F.Nwk.DevIEEE]
                        
                        for each_cluster in each_endpoint[M.F.Dat.Clusters]:
                            if each_cluster[M.F.Dat.DataCluster] == M.Clusters.SM:  # Is this data from the simple metering cluster?
                                for each_attr in each_cluster[M.F.Dat.Attributes]:
                                    if each_attr[M.F.Dat.AttributeID] == VOLTAGE_ATTR_ID:
                                        
                                        print "Node " + str    (this_node_ieee) + " reports a voltage of " + str(float(each_attr[M.F.Dat.Value])/VOLTAGE_ATTR_DIVISOR)
                '''
                
                # Got a message we don't recognise
                print "Received an unrecognised V1.0 message from the ESBox: %s" % json_data
        else:
            # Got a message we don't recognise
            print "Received an invalid V1.0 message from the ESBox: %s" % json_data
        
                          
                        
def process_protocol_1_1(json_data):        
    if M.F.Gen.ESBoxVersion_1_1 in json_data:
        print "[1.1] ESBox with version " + json_data[M.F.Gen.ESBoxVersion_1_1] + " sent some data."
        
        if M.F.Gen.Messages_1_1 in json_data:
            # Here is where we parse V1.1 protocol messages
            for each_message in json_data[M.F.Gen.Messages_1_1]:
                # Check for a 'no further messages' message
                if each_message[M.F.Gen.MsgID_1_1] == M.SS_ESB.E.NoFurtherMessages_1_1:
                    print "\tNo further messages."
                    continue
                
                # Check for a 'SendData' message
                if (each_message[M.F.Gen.MsgID_1_1] == M.SS_ESB.E.SendData):
                    
                    # Check that the data 'source' is the latest readings
                    if each_message[M.F.Dat.Source] == M.V.Dat.Source.LatestReadings_1_1:
                        
                        # The latest readings message data list (see ExampleMessages_8834.py line 3479) will contain a number of entries for each HAN/Endpoint pair
                        # for which latest readings were available
                        for each_han_endpoint in each_message[M.F.Dat.Data_1_1]:
                            
                            this_node_ieee = each_han_endpoint[M.F.Nwk.HAN_1_1]
                            this_endpoint_id = each_han_endpoint[M.F.Nwk.EndpointID_1_1]
                            
                            print "\tReceived readings for device %s:%d" % (this_node_ieee, this_endpoint_id) 
                            
                            for each_cluster in each_han_endpoint[M.F.Dat.Clusters_1_1]:
                                if each_cluster[M.F.Gen.Cluster_1_1] == M.Clusters_1_1.SM:  # Is this data from the simple metering cluster?
                                    for each_attr in each_cluster[M.F.Dat.Attributes_1_1]:
                                        if each_attr[M.F.Dat.AttributeID_1_1] == VOLTAGE_ATTR_ID:
                                            print "\t\tVoltage: " + str(float(each_attr[M.F.Dat.Data_1_1])/VOLTAGE_ATTR_DIVISOR)
                    # Continue on to process next message in wrapper
                    continue   
                
                # Got a message we don't recognise
                print "Received an unrecognised V1.1 message from the ESBox: %s" % json_data
        else:
            # Got a message we don't recognise
            print "Received an invalid V1.1 message from the ESBox: %s" % json_data
    
class TestServer(resource.Resource):
    isLeaf = True
    
    num_get_requests = 0
    time_of_last_readings = time.time()-10
    
    def render_GET(self, request):
        self.numberGETRequests += 1
        request.setHeader("content-type", "text/plain")
        print "Have been visited by a web browser " + str(self.num_get_requests) + " times!"
        return "Hello there! You're not an ESBox!\n"
    
    def render_PUT(self, request):
        
        print "\n"
        
        # Read the content of the PUT request
        data = request.content.read()
        
        # We'll try to decode JSON sent by the ESBox here
        try:
            decoded_json = json.loads(data)            
            # Send it elsewhere for processing          
        except:
            print "Couldn't decode valid JSON from the ESBox message wrapper :("
            return
         
        process_data(decoded_json)
     
        # Prepare the response message and container for the ESBox
        request.setHeader("content-type", "application/json")
        
        # For now we're just going to see if it's been more than 10 seconds since we last requested latest readings, and if so we'll send a 
        # GetData message and ask for the latest readings. Otherwise, we'll just close the connection.
        if time.time() - self.time_of_last_readings > 10:
            print "Requesting latest readings."
            response_message = generate_get_latest_readings()
            #print "Toggle device relay."
            #esponse_message = toggle_relay()
            self.time_of_last_readings = time.time()
        else:
            print "Closing connection to ESBox."
            response_message = generate_close_connection()
        response_container = generate_container( [response_message] )
        
        print "Sent following message to ESBox: %s" % str(response_container)
        return json.dumps(response_container)
    
reactor.listenTCP(SERVER_PORT, server.Site(TestServer()))
reactor.run()