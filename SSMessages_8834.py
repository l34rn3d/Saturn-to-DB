#********************************************************************
# SSMessages.py
# Copyright 2015, Saturn South Pty Ltd
#
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


# This file contains constant definitions relating to the ESBox API
# protocol versions 1.0 and 1.1 (beta).
# Constants available in API protocol version 1.0 or later only are
# not suffixed.
# Constants available in API protocol version 1.1 or later only are
# suffixed with _1_1.
# Please refer to ExampleMessages.py for usage notes and detailed
# descriptions of meanings etc.


# Message ID definitions:

class Common():
    # Messages that are shared between many clusters
    
    class E():
        # Message IDs
        
        # ESCo -> ESBox
        ReadAttributes = "ReadAttributes"
        ReadAttributes_1_1 = "RA"

        WriteAttributes = "WriteAttributes"
        WriteAttributes_1_1 = "WA"

        
class SS_ESB():
    # Saturn South ESBox cluster
    
    class E():
        # Message IDs
        
        # Protocol messages - Common
        NoFurtherMessages = "NoFurtherMessages"
        NoFurtherMessages_1_1 = "NFM"
        # n.b. login data is now supplied in the messages wrapper

        # Protocol messages - ESCo -> ESBox
        NotAuthenticated = "NotAuthenticated"
        NotAuthenticated_1_1 = "NAuth"
        CloseConnection = "CloseConnection"
        CloseConnection_1_1 = "Close"
        GetSupportedVersions_1_1 = "GSV"

        # Protocol messages - ESBox -> ESCo
        SendSupportedVersions_1_1 = "SSV"

        # ESBox Management Messages - Common
        SendErrors = "SendErrors"
        SendErrors_1_1 = "SEr"

        # ESBox Management Messages - ESCo -> ESBox
        GetESBoxOptions = "GetESBoxOptions"
        GetESBoxOptions_1_1 = "GEO"

        SetESBoxOptions = "SetESBoxOptions"
        SetESBoxOptions_1_1 = "SEO"

        RestartESBox = "RestartESBox"
        SendUpdateToken = "SendUpdateToken"
        GetUpdateStatus_1_1 = "GetUpdateStatus"
        GetErrors = "GetErrors"

        GetStatus_1_1 = "GSta"

        ExecuteTerminalCommand_1_1 = "ExTrm"
        GetTerminalOutput_1_1 = "GTrm"
        GetDir_1_1 = "GDir"
        GetFile_1_1 = "GFil"
        ExecuteFilesystemOperation_1_1 = "FSOp"
        SendFilesystemOperationResult_1_1 = "SFSR"

        # ESBox Management Messages - ESBox -> ESCo
        SendESBoxOptions = "SendESBoxOptions"
        SendESBoxOptions_1_1 = "SEOpts"
        SendUpdateStatus_1_1 = "SUpdSta"
        SendTerminalOutput_1_1 = "STrm"
        SendDir_1_1 = "SDir"
        SendFile_1_1 = "SFil"

        SendStatus_1_1 = "SSta"

        # ZigBee Network Management Messages - ESCo -> ESBox
        GetDeviceList = "GetDeviceList"
        GetDeviceList_1_1 = "GDL"
        RequestDeviceToLeave = "RequestDeviceToLeave"
        LocateDevice = "LocateDevice"
        PermitJoining = "PermitJoining"
        ExecuteDeviceManagementOperation_1_1 = "EDMO"

        # ZigBee Network Management Messages - ESBox -> ESCo
        SendDeviceList = "SendDeviceList"
        SendDeviceList_1_1 = "SDv"
        SendDeviceManagementResult_1_1 = "SDMR"

        # Database Management Messages - ESCo -> ESBox
        GetAvailableData = "GetAvailableData"
        GetData = "GetData"
        GetData_1_1 = "GD"
        GetLatestReadings = "GetLatestReadings"
        ClearDatabase = "ClearDatabase"
        ConfigureDataLogging = "ConfigureDataLogging"

        # Data Transfer Messages - ESBox -> ESCo
        SendAvailableData = "SendAvailableData"
        SendData = "SendData"
        SendLatestReadings = "SendLatestReadings"

        
class SS_LC():
	# Saturn South Load Control cluster
    
    class E():
        # Message IDs
    
        # ESCo -> ESBox
        GetWaveform = "GetWaveform"
        BroadcastDispatch = "BroadcastDispatch"

        # ESBox -> ESCo
        DispatchReport = "DispatchReport"
        UFLSReport = "UFLSReport"

        
class OnOff():
    # Zigbee Switch/OnOff Cluster
    
    class E():
        # Message IDs
        
        # ESCo -> ESBox
        SwitchState = "SwitchState"
        SwitchState_1_1 = "SwSt"


        
# Field name definitions:

class F():

    class Gen():
        # General field names
    
        MsgID = "MsgID"
        MsgID_1_1 = "M"

        Cluster = "Cluster"
        Cluster_1_1 = "Cl"

        ClusterID = "ClusterID"
        ClusterID_1_1 = "I"

        ClusterManufacturer = "ClusterMfctr"
        ClusterManufacturer_1_1 = "M"

        ProtocolVersion = "ProtocolVersion"
        ProtocolVersion_1_1 = "PVer"

        ProtocolVersions_1_1 = "Vers"

        Messages = "Messages"
        Messages_1_1 = "Msgs"

        Auth = "Auth"

        ESBoxVersion = "ESBoxVersion"
        ESBoxVersion_1_1 = "EVer"
        
        Operation_1_1 = "Op"
        Result_1_1 = "Rs"
        
        Details_1_1 = "Dtl"
        
        Enable_1_1 = "En"

    class Nwk():
        # Zigbee network related field names
        
        Version = "Version"
        Version_1_1 = "V"
        UpdateStatus = "UpdateStatus"
        Detailed = "Detailed"
        Detailed_1_1 = "Dtl"
        DeviceList = "DeviceList"
        DeviceList_1_1 = "Dvs"
        
        Neighbours_1_1 = "Nbr"
        PANAddr_1_1 = "PAN"
        NwkAddr_1_1 = "Nwk"
        DeviceProperties_1_1 = "Prp"
        PermitJoiningEnabled_1_1 = "PJ"
        Depth_1_1 = "Dp"
        
        IsCoordForThisESBox_1_1 = "TZc"

        DevIEEE = "DevIEEE"
        HAN_1_1 = "HAN"

        ModelID = "ModelID"
        ModelID_1_1 = "Mdl"
        ModelList = "ModelList"
        ManufacturerName = "ManufacturerName"
        ManufacturerName_1_1 = "Man"
        DeviceID = "DeviceID"
        LocationDescription = "LocationDescription"
        LocationDescription_1_1 = "Loc"
        LastContact = "LastContact"
        LastContact_1_1 = "Con"
        JoinTime = "JoinTime"
        JoinTime_1_1 = "Jn"
        LastRejoinTime = "LastRejoinTime"
        LastRejoinTime_1_1 = "RJn"
        OnlineStatus = "OnlineStatus"
        OnlineStatus_1_1 = "OL"
        NodeType = "NodeType"
        NodeType_1_1 = "NdT"
        Children = "Children"
        Children_1_1 = "Cld"
        Endpoints = "Endpoints"
        Endpoints_1_1 = "EPs"

        EndpointID = "EndpointID"
        EndpointID_1_1 = "EP"

        LoggedAttributes = "LoggedAttributes"
        DestCluster = "DestCluster"
        LogAttributeIDs = "LogAttributeIDs"
        BindConfiguration = "BindConfiguration"
        TargetIEEE = "TargetIEEE"
        TargetEndpoint = "TargetEndpoint"
        ClusterOrGroup = "ClusterOrGroup"
        ClusterOrGroupID = "ClusterOrGroupID"
        ClusterID = "ClusterID"
        MinInterval = "MinInterval"
        MaxInterval = "MaxInterval"
        AttrList = "AttrList"
        AttrID = "AttrID"
        MinChange = "MinChange"
        LQI = "LQI"
        CoordLQI_1_1 = "C"
        EndDeviceLQI_1_1 = "N"
        AddRemove = "AddRemove"
        GroupID = "GroupID"
        DestIEEE = "DestIEEE"
        DestEndpointID = "DestEndpointID"
        SourceIEEE = "SourceIEEE"
        SourceEndpointID = "SourceEndpointID"
        DeviceManufacturerName = "DeviceManufacturerName"
        Devices = "Devices"
        ReportConfiguration = "ReportConfiguration"
        Revert = "Revert"

        class Short():
            # Deprecated
            #
            # aliased field names, but shortened for more practical transmission and usage
            # new in v1.1
            DevIEEE = "IEEE"
            EndpointID = "EP"

    class Db3():
        # Deprecated in v1.1 onwards (still used for some v1.0 messages)
        #
        # added as part of v1.0 spec
        # TODO: deprecated in this location (deprecate in v1.1)
        # field labels
        Data = "D"
        Attributes = "A"
        TimeChange = "T"
        DiscardedData = "J" # J stands for junk ;)

    class Dat():
        # Field names related to data transmission etc.
    
        Duration = "Duration"
        Duration_1_1 = "Dur"
        Interval_1_1 = "Ivl"
        DataCluster = "DataCluster"
        DataTime = "DataTime"
        StartTime = "StartTime"
        EndTime = "EndTime"
        Data = "Data"
        Data_1_1 = "D"
        Clusters = "Clusters"
        Clusters_1_1 = "Cls"

        Mode_1_1 = "Md"

        Attributes = "Attributes"
        Attributes_1_1 = "Ats"

        SampleLength = "SampleLength"

        AttributeID = "AttributeID"
        AttributeID_1_1 = "I"

        Value = "Value"
        Value_1_1 = "V"

        MinimumValue_1_1 = "Mn"
        MaximumValue_1_1 = "Mx"

        DeltaTime = "DTime" # <- used as v1.0 constant to maintain compatibility with legacy test/debug implementation
        DeltaTime_1_1 = "DTm"
        Time = "Time" # <- used as v1.0 constant to maintain compatibility with legacy test/debug implementation
        Time_1_1 = "Tm"
        Type_1_1 = "Tp"
        Source = "Src"

        # For more compact display of clusters
		# Deprecated in v1.1 onwards (still used for some v1.0 messages)
        DataClusterId = "CluId" # new in v1.1
        DataClusterManufacturer = "CluMan" # new in v1.1

        class Short():
            # Deprecated in v1.1 onwards (still used for some v1.0 messages)
            #
            # aliased field names, but shortened for more practical transmission and usage
            # add in v1.1

            Attributes = "Attrs"
            AttributeID = "ID"
            Value  = "V"
            Type = "T"

        class Waveform():
            Source = "Source"
            Trigger = "Trigger"
            SampleRate = "SampleRate"
            SampleResolution = "SampleResolution"

            VoltageSamples = "VoltageSamples"
            CurrentSamples = "CurrentSamples"

        class Db3(): # added as part of v1.0 spec
            # moved to Dat.* as part of v1.1 spec
            # field labels
            Data = "D"
            Attributes = "A"
            TimeChange = "T"
            DiscardedData = "J" # J for junk

        class Sdb():
            Fifo = "Fifo"
            Cells = "Cells"
            NCells = "NCel"
            DelIeee = "DI"
            DelEP = "DE"
            DelClu = "DC"
            DelTime = "DT"

    class ESB():
        Options = "Options"
        Options_1_1 = "Opt"
        Errors = "Errors"
        Errors_1_1 = "Ers"
        Error = "Error"
        Error_1_1 = "Er"

        Status = "Status"
        Status_1_1 = "Sta"
        AppStatus = "App"
        ZigbeeStatus = "Zigbee"
        ZigbeeStatus_1_1 = "ZB"

        ServerRequests = "ServReqs"

        Cmd = "Cmd"
        Dir = "Dir"
        File_1_1 = "File"
        Recurse = "Recurse"
    
        # Terminal
        Term = "term"
        Term_1_1 = "Trm"
        TermData = "data"
        TermData_1_1 = "Dat"
        TermForegroundColor = "fg"
        TermForegroundColor_1_1 = "FG"
        TermBackgroundColor = "bg"
        TermBackgroundColor_1_1 = "BG"
        TermBold = "fb"
        TermBold_1_1 = "B"
        TermItalic = "fi"
        TermItalic_1_1 = "I"
        TermLeading = "lead"
        TermLeading_1_1 = "Ld"
        TermNewline = "nl"
        TermNewline_1_1 = "NL"
        TermPriority = "pri"
        TermPriority_1_1 = "Pri"
        TermUid = "uid"
        TermUid_1_1 = "Uid"
        TermMaxLines = "maxl"
        TermMaxLines_1_1 = "MxL"

        TermCommand_1_1 = "Cmd" # base64 encoded -- takes precedence over raw command
        TermCommandRaw_1_1 = "CmdRaw" # no special encoding

        class Filesystem():
            
            Code_1_1 = "Cd"
            Path_1_1 = "Pth"
            List_1_1 = "Lst"
            Contents_1_1 = "Cnt"
            
            Name_1_1 = "N"
            Time_1_1 = "T"
            Date_1_1 = "D"
            Size_1_1 = "S"
            
            IsReadOnly_1_1 = "RO"
            IsHidden_1_1 = "Hi"
            IsSystem_1_1 = "Sy"
            IsVolumeLabel_1_1 = "Vo"
            IsLongFileNameEntry_1_1 = "LF"
            IsDirectory_1_1 = "Di"
            IsArchive_1_1 = "Ar"
            
            MakeParents_1_1 = "P"
            Recursive_1_1 = "R"
            Force_1_1 = "F"
            Overwrite_1_1 = "O"
            Append_1_1 = "A"


        class Update():
                
            # Updates
            Current_1_1 = "Cur" # this includes downloading updates from server, realtime progress on ota updates and progress flashing bootloader updates etc.
            OTARegistered_1_1 = "OTA" # n.b. this includes coordinator updates
            ESBoxAllPending_1_1 = "Pend" # this includes filesystem, userspace and bootloader updates
            
            # -- registered
            Path_1_1 = "Path" # path of registered update (unix timestamp)
            ExpiryTime_1_1 = "ExpT" # expiry time of registered update (unix timestamp)
            AddedTime_1_1 = "AddT" # added time of registered update (unix timestamp)
            
            Updates_1_1 = "Upd" # list of registered updates
            
            # -- current
            CurrentOTAUpdates_1_1 = "OTA" # holds information about the current OTA update(s) being processed
            CurrentDownloads_1_1 = "DL" # holds information about the current update(s) being downloaded from an update server
            
            
            # fields used within CurrentOTAUpdates_x_x
            OTAPercentComplete_1_1 = "Pct"
            OTAEstimatedSecondsRemaining_1_1 = "Rem"
            OTAType_1_1 = "Typ"
        
        
            # fields used within CurrentDownloads_x_x
            DownloadStatus_1_1 = "Sta"
            DownloadFilename_1_1 = "FN"
            DownloadSavepath_1_1 = "Pth"
            DownloadMD5_1_1 = "MD5"
            DownloadSizeBytes_1_1 = "Sz"
            DownloadDoneBytes_1_1 = "DL"


    class SSLC():
        FrequencyOfDisconnect = "Freq"
        FrequencyOfDisconnect_1_1 = "F"

    class OnOff():
        Action = "Action"


    class Upd():
        Token = "Token"
        Token_1_1 = "T"
        
        # Update token internal json fields
        Addr = "a"
        Port = "p"
        Path = "t"
        ProxyAddr = "x"
        ProxyPort = "q"
        ProxyUsername = "u"
        ProxyPassword = "w"
        UpdateId = "i"

        UpdateDevIeee = "d"

        UpdateDevVersions = "v"

        UpdateType = "y"

        Md5 = "h"

        # ONLY THE FIRST item in a manifest may have a meta field,
        # meta fields in other items should be ignored.
        # -- n.b. that the meta field is ALWAYS optional
        Meta = "m"

        # meta fields
        MetaRetryAfter = "r"
        MetaUsingId = "i"

    # Settings
    class S():
        class ESBox():

            # Read/Write
            PollESCoInterval = "PollESCoIntvl"
            ESCoTimeout = "PollESCoTimeout"
            PrimaryESCoAddress = "PrimESCoAddr"
            PrimaryESCoPath = "PrimESCoPath"
            PrimaryESCoPort = "PrimESCoPort"
            SecondaryESCoAddress = "SecESCoAddr"
            SecondaryESCoPath = "SecESCoPath"
            SecondaryESCoPort = "SecESCoPort"
            ProxyAddr = "ProxyAddr"
            ProxyPort = "ProxyPort"
            ProxyUsername = "ProxyUsername"
            ProxyPassword = "ProxyPassword"
            EnableAsynchronousContainers = "EnableAsynchronousContainers"
            AutomaticallySendLatestReadings = "AutomaticallySendLatestReadings"
            NoESCoCommsSafeStateTimeout = "TimeoutNoESCoComms"
            CurrentTime = "CurrentTime"
            # db
            DbMaxReportedEsboxTimeDiff = "DbMaxReportedEsboxTimeDiff"
            DbCreateNewFileThreshold = "DbCreateNewFileThreshold"
            DbWriteDiscardedDatapoints = "DbWriteDiscardedDatapoints"

            # Read only
            TotalUptimeMs = "TotalUptimeMs"
            ThisUptimeMs = "ThisUptimeMs"
            LastGoodESCoAddress = "LastGoodESCoAddr"
            LastGoodESCoPath = "LastGoodESCoPath"
            LastGoodESCoPort = "LastGoodESCoPort"
            LastGoodProxyAddr = "LastGoodProxyAddr"
            LastGoodProxyPort = "LastGoodProxyPort"
            NumReboots = "NumReboots"
            NumSoftReboots = "NumSoftReboots"
            NumWatchdogReboots = "NumWatchdogReboots"
            NumCmdsProcessed = "NumCmdsProcessed"
            NumCmdsFailed = "NumCmdsFailed"
            NumCmdsUnrecognised = "NumCmdsUnrecognised"
            NumHTTPConnectionsFailed = "NumHTTPConnectionsFailed"
            NumSSLConnectionsFailed = "NumSSLConnectionsFailed"
            SoftReboot = "SoftReboot"

            # Write Only (new in v1.1)
            WriteToNvm = "WrNVM" # If set by esco (0/non-zero int),
                                 # key settings will be saved to backup
                                 # NVM (this should be set (very) infrequently,
                                 # only when connection settings change in
                                 # critical ways or else the PIC's flash
                                 # will be destroyed)


# Values:

class V():

    Version = "1.0"
    SubVersion = "1" # updated for minor, non-serious, but potentially breaking changes

    class Upd():
        UpdateTypeUserspace     = "U"
        UpdateTypeBootloader1   = "B"
        UpdateTypeCoord         = "C" # n.b. this was changed from UpdatetypeCoord as of version 7860. The value has remained the same.
        UpdateTypeOTA           = "O"
        UpdateTypeFS            = "F"
        
    class Nwk():
        Online = "Online"
        Online_1_1 = "On"
        Refresh = "Refresh"
        Refresh_1_1 = "Rfr"
        Offline = "Offline"
        Offline_1_1 = "Off"
        Unknown = "Unknown"
        Unknown_1_1 = "Ukn"
        ZigBeeCoordinator = "Zc" # This constant name may change (value will remain the same)
        ZigBeeRouter = "Zr" # This constant name may change (value will remain the same)
        ZigBeeEndDevice = "Zed" # This constant name may change (value will remain the same)
        Add = "Add"
        Remove = "Remove"
        Bind = "Bind"
        Unbind = "Unbind"
        Cluster = "Cluster"
        Group = "Group"
        
        class PJ():
			TurnOff_1_1 = 0
			TurnOn_1_1 = 1
			Toggle_1_1 = 2 # default
        
        class Op():
            ScanDeviceList_1_1 = "SDL"
            RebuildDeviceList_1_1 = "RDL"
            PermitJoining_1_1 = "PJ"
            ClearOTAUpdateRegistry_1_1 = "CUR"
            ClearDeviceRegistry_1_1 = "CDR"
            FactoryReset_1_1 = "FR"
            LocateEndDevice_1_1 = "Loc"
            LeaveEndDevice_1_1 = "Lv"
            RebootEndDevice_1_1 = "Rbt"
            RefreshEndDevice_1_1 = "Rfr"
            LQITestEndDevice_1_1 = "LQI"
            OverrideReportInterval_1_1 = "ORI"

            class Err():
                SUCCESS        = 0
                UNKNOWN_ERROR  = 1
                NO_OP          = 2
                BAD_OP         = 3
                OP_FAILED      = 4
            
    class OnOff():
        On = "On"
        Off = "Off"
        Toggle = "Toggle"

    class Err():
        Priority_Fatal          =  0
        Priority_High           =  1
        Priority_Medium         =  2
        Priority_Low            =  3
        Priority_Warning        =  4
        Priority_SelectAll      = -1

        # Filesystem errors (fresult) (more errors are possible - request further information from
        # Saturn South if other filesystem errors are encountered)
        DISK_ERROR_FATAL        = 0     # low level disk error
        DISK_ERROR              = 1     # disk error, possibly not fatal
        DISK_LOCKED             = 2     # disk has hardware write-lock set
        NO_FS                   = 3     # disk is not formated
        FS_ERROR                = 4     # other critical file-system failure
        # rtc errors
        RTC_ERROR               = 5     # RTC failed and is inoperable
        # comms errors
        ETHERNET_NOT_CONNECTED  = 6     # ethernet not connected
        ETHERNET_ERROR          = 7     # ethernet suffered a fatal error
        COMMS_ERROR             = 8     # failed communicating with the esco / target communication platform
        # zigbee errors
        ZIGBEE_ERROR            = 9     # ethernet not connected
        # internal errors
        OUT_OF_MEMORY           = 10    # system ran out of heap
        FATAL_UPDATER_ERROR     = 11    # a fatal update failure occurred
        UNKNOWN                 = 12    # an error occurred but there are no details for it
        # application errors
        FS_VERSION_SRV_BAD      = 13    # filesystem (srv) has diverged from its allowed parameters and needs replacing

    class Status():
        AppError = 0
        AppUpdating = 1
        AppOK = 2

        ZigbeeError = 0
        ZigbeeStarting = 1
        ZigbeePJ = 2
        ZigbeeOK = 3

    class Dat():
        # added v1.1
        class Type():
            # n.b these are to kept up-to-date with db3_datatype_t
            Int         = "i"
            Uint        = "u"
            String      = "s"
            Byte        = "b"
            Raw         = "r"
            Timechange  = "t"

        class Source():
            Sdb         = "S"
            Db3         = "D"
            LatestReadings_1_1 = "L"

    class Waveform():
        class Source():
            Voltage = 0
            Current = 1
            VoltageAndCurrent = 2

        class Trigger():
            Random = 0
            VoltageZeroCross = 1
            RelayStateChange = 2

        class SampleRate():
            sr512 = 0
            sr1024 = 1
            sr2048 = 2
            sr4096 = 3

        class SampleResolution():
            eight = 0
            sixteen = 1
            
        class VoltageByte():
            LSB = 0
            MSB = 1
                
        class CurrentByte():
            LSB = 0
            MSB = 1

    class Term():
        class Pri():
            Normal = 0
            Meta = 1 # -- this message should not be displayed, it is a control message
            Debug = 2
            Notification = 3
            Warning = 4
            Error = 5
            FatalError = 6
            
            
    class Filesystem():
        
        # filesystem operations
        MakeDir_1_1 = "MkD"
        Remove_1_1 = "Rm"
        MakeFile_1_1 = "MkF"
        WriteFile_1_1 = "WF"
        WriteFileFromRemote_1_1 = "WFR"
        
        # must be single chars
        MakeParents_1_1 = "P"
        Recursive_1_1 = "R"
        Force_1_1 = "F"
        Overwrite_1_1 = "O"
        Append_1_1 = "A"
        

# Clusters:

# - Individual cluster manufacturer/id values
# - See class 'Clusters' for combined dict representations
class ClusterParts():
    class SS_ESB():
        ClusterId = 0
        ClusterManufacturer = 4278
    class SS_LC():
        ClusterId = 64784
        ClusterManufacturer = 4278
    class OnOff():
        ClusterId = 6
        ClusterManufacturer = 0
    class SM():
        ClusterId = 1794
        ClusterManufacturer = 0
    class Basic():
        ClusterId = 1
        ClusterManufacturer = 0
    class Common():
        # match anything special case
        ClusterId = -1
        ClusterManufacturer = -1

        
# Cluster descriptions:
class Clusters():
    SS_ESB = {
        F.Gen.ClusterID : ClusterParts.SS_ESB.ClusterId,
        F.Gen.ClusterManufacturer : ClusterParts.SS_ESB.ClusterManufacturer
    }

    SS_LC = {
        F.Gen.ClusterID : ClusterParts.SS_LC.ClusterId,
        F.Gen.ClusterManufacturer : ClusterParts.SS_LC.ClusterManufacturer
    }

    OnOff = {
        F.Gen.ClusterID : ClusterParts.OnOff.ClusterId,
        F.Gen.ClusterManufacturer : ClusterParts.OnOff.ClusterManufacturer
    }

    SM = {
        F.Gen.ClusterID : ClusterParts.SM.ClusterId,
        F.Gen.ClusterManufacturer : ClusterParts.SM.ClusterManufacturer
    }

    Basic = {
        F.Gen.ClusterID : ClusterParts.Basic.ClusterId,
        F.Gen.ClusterManufacturer : ClusterParts.Basic.ClusterManufacturer
    }

# Cluster descriptions:
class Clusters_1_1():
    SS_ESB = {
        F.Gen.ClusterID_1_1 : ClusterParts.SS_ESB.ClusterId,
        F.Gen.ClusterManufacturer_1_1 : ClusterParts.SS_ESB.ClusterManufacturer
    }

    SS_LC = {
        F.Gen.ClusterID_1_1 : ClusterParts.SS_LC.ClusterId,
        F.Gen.ClusterManufacturer_1_1 : ClusterParts.SS_LC.ClusterManufacturer
    }

    OnOff = {
        F.Gen.ClusterID_1_1 : ClusterParts.OnOff.ClusterId,
        F.Gen.ClusterManufacturer_1_1 : ClusterParts.OnOff.ClusterManufacturer
    }

    SM = {
        F.Gen.ClusterID_1_1 : ClusterParts.SM.ClusterId,
        F.Gen.ClusterManufacturer_1_1 : ClusterParts.SM.ClusterManufacturer
    }

    Basic = {
        F.Gen.ClusterID_1_1 : ClusterParts.Basic.ClusterId,
        F.Gen.ClusterManufacturer_1_1 : ClusterParts.Basic.ClusterManufacturer
    }

