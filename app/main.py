import sys, logging, threading
from typing import List
import time
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

# IMPORTANT Path to IHC_PMS_Lib dlls
sys.path.append("/home/for/dev/IHC_PMS_Lib_1.9.2.0/bin")
from ihcWrappers import *


def main():
    print("### IHC_PMS_Lib Test Script ###")
    print("Configuration:")
    print("ODTC: " + config['IHC']['ODTC'])
    print("SCILA: " + config['IHC']['SCILA'])
    print("PMS version: " + PmsWrapper.GetAssemblyVerion())
    
    pms = PmsWrapper()
    # pms.IpAddressIndex(1) #e.g. Linux VPN (multihomed adapter ip index)

    nics = pms.GetSupportedNICs() #default wired ethernet
    #nics = pms.GetSupportedNICs(NetworkInterfaceTypesWrapper.Vpn) # Windows VPN
    if len(nics) == 0:
        nics = pms.GetSupportedNICs(NetworkInterfaceTypesWrapper.WiredEthernet + NetworkInterfaceTypesWrapper.VirtualEthernet)
    if len(nics) > 1:
        nics = pms.GetSupportedNICs(NetworkInterfaceTypesWrapper.Vpn)
    for nic in nics:
        print("Network interface: " + nic.Id + " " + nic.Name + " " + nic.Description)
    # alt static
    #nics = PmsWrapper.SupportedNICs(NetworkInterfaceTypesWrapper.WiredEthernet)
    
    if len(nics) == 1:
        eru = pms.StartEventReceiver(nics[0].Id) # Explicit Id
    else:
        # manually choose an Id
        eru = pms.StartEventReceiver(nics[1].Id)
    print("EventReceiver Uri: " + eru)

    
    '''SCILA'''
    if config['IHC']['SCILA'] == "True":
        print("SCILA Dll Version: " + ScilaWrapper.GetAssemblyVersion())
        deviceIp = "192.168.1.128" # predefined scila ip

        # Finder
        frScilas = ScilaFinderWrapper.SearchDevices()
        if len(frScilas) == 0:
            print("No SCILA found")
        for val in frScilas:
            print("Finder result: " + val.Name + " " + str(val.WsdlUri))
            # Gather device info before Create()
            status = PmsWrapper.GetStatus(val.IPv4Address)
            print(val.Name + " state: " + status.State)
            print(val.Name + " locked: " + status.Locked)
            (r, di) = PmsWrapper.GetDeviceIdentification(val.IPv4Address)
            assert r.ReturnCode == 1
            print(val.Name + " pre-connect GetDeviceIdentification: " + di.DeviceName + " " + di.Wsdl + " " + di.DeviceFirmwareVersion)

        status = PmsWrapper.GetStatus(deviceIp)
        (r, di) = PmsWrapper.GetDeviceIdentification(deviceIp)
        assert r.ReturnCode == 1

        # Download logs and latest trace file
        print("Start log/trace download...")
        error = DownloadScilaLogTraces(ip=deviceIp, path="/home/for/dev/logDownload/" + di.DeviceName, traceFileCount=1, logs=True)
        assert(error is None)
        print("log/trace download finished")

        # Create device
        try:
            scila = pms.Create("http://" + deviceIp + "/scila.wsdl")
        except Exception as ex:
            if (ex.Message) == "Invalid lockId.":
                scila = pms.Create("http://" + deviceIp + "/scila.wsdl", "myLockId")
            else:
                raise
        # Register Callback(s)
        scila.RegisterStatusEventCallback(OnStatusEvent)
        print("Device Name: " + scila.DeviceName)
        print("Current LockId: " + str(scila.LockId))
        di = GetDeviceIdentification(scila)
        assert di.DeviceName == scila.DeviceName
        s = GetStatus(scila)
        assert s.State != "InError"
        # SiLA Commands
        rv = scila.Reset()
        assert rv.Success == True
        # if rv.Success == False:
        #     print("SCILA Reset error: " + rv.Message)
        #     print("Exit")
        #     return
        s = GetStatus(scila)
        assert s.State == "Standby"
        # Lock device
        scila.LockId = "myLockId"
        rv = scila.LockDevice()
        assert rv.Success == True
        # Test lock
        s = GetStatus(scila)
        assert s.Locked == True
        scila.LockId = None # Set Wrong lockId
        rv = scila.GetConfiguration()
        assert rv.Success == False
        # Unlock device
        scila.LockId = "myLockId"
        rv = scila.UnlockDevice()
        assert rv.Success == True
        s = GetStatus(scila)
        assert s.Locked == False
        # GetConfiguration
        rv = scila.GetConfiguration()
        assert rv.Success == True
        print(rv.ResponseData.LogLevel)
        print(rv.ResponseData.NetworkConfig)
        print(rv.ResponseData.SoapCompression)
        print(rv.ResponseData.SysDateTime)
        print(rv.ResponseData.UseDeviceClassDateTime)
        # Configure Device example: import Network-Settings from file
        cx = ScilaConfigXmlWrapper()
        cx.ImportNetworkConfigXml("dhcp.xml")
        print(cx.GetParamsXml())
        # SetConfiguration
        rv = scila.SetConfiguration(cx.GetParamsXml())
        assert rv.Success == True
        # Initialize
        rv = scila.Initialize()
        assert rv.Success == True
        s = GetStatus(scila)
        assert s.State == "Idle"
        # Delay 1s
        rv = scila.Delay(1)
        assert rv.Success == True
        # GetAutoBoostCo2
        rv = scila.GetAutoBoostCo2()
        assert rv.Success == True
        print(rv.ResponseData.AutoBoostCO2)
        print(rv.ResponseData.BoostState)
        # GetCo2FlowStatus
        rv = scila.GetCo2FlowStatus()
        assert rv.Success == True
        print(rv.ResponseData.CO2FlowStatus)
        # GetDoorStatus
        rv = scila.GetDoorStatus()
        assert rv.Success == True
        print(rv.ResponseData.Drawer1)
        print(rv.ResponseData.Drawer2)
        print(rv.ResponseData.Drawer3)
        print(rv.ResponseData.Drawer4)
        # GetLiquidLevel
        rv = scila.GetLiquidLevel()
        assert rv.Success == True
        print(rv.ResponseData.LiquidLevel)
        # GetParameters
        rv = scila.GetParameters()
        assert rv.Success == True
        print(rv.ResponseData.Position)
        print(rv.ResponseData.WorkstationMode)
        # New Parameters config example
        px = ScilaParamsXmlWrapper()
        px.Position = 1
        px.WorkstationMode = False
        print(px.GetParamsXml())
        # SetParameters
        rv = scila.SetParameters(px.GetParamsXml())
        assert rv.Success == True
        # GetTemperature
        rv = scila.GetTemperature()
        assert rv.Success == True
        print(rv.ResponseData.CurrentTemperature)
        print(rv.ResponseData.TargetTemperature)
        print(rv.ResponseData.TemperatureControl)
        # GetValveStatus
        rv = scila.GetValveStatus()
        assert rv.Success == True
        print(rv.ResponseData.Gas_Boost)
        print(rv.ResponseData.Gas_Normal)
        print(rv.ResponseData.H2O)
        # Open-/CloseDoor
        rv = scila.PrepareForInput(4)
        assert rv.Success == True
        rv = scila.OpenDoor()
        assert rv.Success == True
        # invoke StatusEvent: multiple doors
        rv = scila.PrepareForInput(3)
        assert rv.Success == True
        rv = scila.OpenDoor()
        assert rv.Success == False
        # rv = scila.RetrieveByPositionId(2) #TODO Fix CommandException
        # assert rv.Success == True
        # SetAutoBoostCo2
        rv = scila.SetAutoBoostCo2(True)
        assert rv.Success == True
        # SetCo2NormalFlow
        rv = scila.SetCo2NormalFlow(True)
        assert rv.Success == True
        # SetTemperature
        rv = scila.SetTemperature(37, True)
        assert rv.Success == True
        rv = scila.SetTemperature(None, True)
        assert rv.Success == True
        rv = scila.SetTemperature(None, None)
        assert rv.Success == True
        rv = scila.SetTemperature(37, False)
        assert rv.Success == True
        # rv = scila.StoreAtPosition(2) #TODO Fix CommandException
        # assert rv.Success == True
        # Disconnect
        print(scila.DeviceName + " dispose")
        scila.Dispose()


    '''ODTC'''
    if config['IHC']['ODTC'] == "True":
        print("ODTC Dll Version: " + OdtcWrapper.GetAssemblyVersion())
        deviceIp = "192.168.1.195" # predefined odtc ip

        (r, di) = PmsWrapper.GetDeviceIdentification(deviceIp)
        assert r.ReturnCode == 1
        
        status = PmsWrapper.GetStatus(deviceIp)
        print(di.DeviceName + " state: " + status.State)
        print(di.DeviceName + " locked: " + str(status.Locked))
        print(di.DeviceName + " build: " + di.DeviceFirmwareVersion)
        print(di.DeviceName + " fw: " + di.DeviceFirmwareVersion[29:32])
        
        legacy = False
        if int(di.DeviceFirmwareVersion[29:32]) <= 232:
            legacy = True

        if not legacy: # skip finder for incompatible older versions
            frOdtcs = OdtcFinderWrapper.SearchDevices()
            if len(frOdtcs) == 0:
                print("No ODTC found")
            for val in frOdtcs:
                print("Finder result: " + val.Name + " " + str(val.WsdlUri))
                # Gather device info before Create()
                status2 = PmsWrapper.GetStatus(val.IPv4Address)
                print(val.Name + " state: " + status2.State)
                print(val.Name + " locked: " + status2.Locked)
                (r, di2) = PmsWrapper.GetDeviceIdentification(val.IPv4Address)
                assert r.ReturnCode == 1
                print("Pre-connect GetDeviceIdentification: " + di2.DeviceName + " " + di2.Wsdl + " " + di2.DeviceFirmwareVersion)

        # with pms.Create("http://10.2.2.8/odtc.wsdl") as odtc:
        #     odtc.Reset()
        #     odtc.Initialize()

        # Download logs and latest trace file
        print("Start log/trace download...")
        error = DownloadOdtcLogTraces(ip=deviceIp, path="/home/for/dev/logDownload/" + di.DeviceName, traceFileCount=1, logs=True, legacy=legacy)
        assert(error is None)
        print("log/trace download finished")

        # Create device
        try:
            odtc = pms.Create("http://" + deviceIp + "/odtc.wsdl")
        except Exception as ex:
            if (ex.Message) == "Invalid lockId.":
                odtc = pms.Create("http://" + deviceIp + "/odtc.wsdl", "myLockId")
            else:
                raise
        # Register Callback(s)
        odtc.RegisterStatusEventCallback(OnStatusEvent)
        odtc.RegisterDataEventCallback(OnDataEvent)
        print("Device Name: " + odtc.DeviceName)
        print("Current LockId: " + str(odtc.LockId))
        di = GetDeviceIdentification(odtc)
        if legacy == False:
            assert di.DeviceName == odtc.DeviceName
        else:
            assert di.DeviceName == "ODTC"
        s = GetStatus(odtc)
        assert s.State != "InError"
        rv = odtc.Reset()
        assert rv.Success == True
        # if rv.Success == False:
        #     print("ODTC Reset error: " + rv.Message)
        #     print("Exit")
        #     #return
        #     exit()
        s = GetStatus(odtc)
        assert s.State == "Standby"
        # Lock device
        odtc.LockId = "myLockId"
        rv = odtc.LockDevice()
        assert rv.Success == True
        # Test lock
        s = GetStatus(odtc)
        assert s.Locked == True
        odtc.LockId = None # Set Wrong lockId
        rv = odtc.GetConfiguration()
        assert rv.Success == False
        # Unlock device
        odtc.LockId = "myLockId"
        rv = odtc.UnlockDevice()
        assert rv.Success == True
        s = GetStatus(odtc)
        assert s.Locked == False
        rv = odtc.GetConfiguration()
        assert rv.Success == True
        print(rv.ResponseData.LogLevel)
        print(rv.ResponseData.NetworkConfig)
        print(rv.ResponseData.SoapCompression)
        print(rv.ResponseData.SysDateTime)
        print(rv.ResponseData.UseDeviceClassDateTime)
        cx = OdtcConfigXmlWrapper()
        cx.ImportNetworkConfigXml("dhcp.xml")
        print(cx.GetParamsXml())
        rv = odtc.SetConfiguration(cx.GetParamsXml())
        assert rv.Success == True
        rv = odtc.Initialize()
        assert rv.Success == True
        rv = odtc.StopMethod()
        assert rv.Success == True
        time.sleep(0.1) # workaround odtc reports State==Busy
        s = GetStatus(odtc)
        assert s.State == "Idle"
        rv = odtc.GetParameters()
        assert rv.Success == True
        print(rv.ResponseData.CSVSeparatorCharacter)
        print(rv.ResponseData.DynamicPreMethodDuration)
        print(rv.ResponseData.ExecuteMethodDataEvent)
        print(rv.ResponseData.MatchLidTemperatures)
        print(rv.ResponseData.MethodsXML)
        for pm in rv.ResponseData.GetPreMethodNames():
            print(pm)
        for m in rv.ResponseData.GetMethodNames():
            print(m)
        px = OdtcParamsXmlWrapper()
        px.ImportMethodSetXml("methodSet-example.xml")
        print(px.GetParamsXml())
        rv = odtc.SetParameters(px.GetParamsXml())
        assert rv.Success == True
        rv = odtc.StopMethod()
        assert rv.Success == True
        rv = odtc.GetLastData()
        assert rv.Success == True
        print(rv.ResponseData.Name)
        print(rv.ResponseData.Data)
        rv = odtc.ReadActualTemperature()
        assert rv.Success == True
        at = rv.ResponseData.SensorValues 
        print("Mount: " + str(at.Mount / 100))
        print("Lid: " + str(at.Lid / 100))
        print(at)
        t = threading.Thread(target=PollRAT, args=(odtc,))
        t.start()
        print("ExecuteMethod")
        rv = odtc.ExecuteMethod("PRE25")
        assert rv.Success == True # PollRat-Thread invokes StopMethod() after x iterations
        print("ExecuteMethod finished")
        print("OpenDoor")
        rv = odtc.OpenDoor()
        assert rv.Success == True
        print("OpenDoor finished")
        print("CloseDoor")
        rv = odtc.CloseDoor()
        assert rv.Success == True
        print("CloseDoor finished")
        t.join()
        print(odtc.DeviceName + " dispose")
        odtc.Dispose()
    
    #input("Press Enter to continue...")
    print("Exit")

def GetStatus(device: DeviceWrapper) -> StatusWrapper:
    if device is None:
        raise TypeError
    (r, s) = device.GetStatus()
    assert r.ReturnCode == 1
    logging.debug(s.DeviceId + " " + s.CurrentTime + " " + str(s.Locked) + (" " + s.PMSId if s.PMSId else "") + " " + s.State)
    #logging.debug(s.SubStates)
    return s

def GetDeviceIdentification(device: DeviceWrapper) -> DeviceIdentificationWrapper:
    if device is None:
        raise TypeError
    (r, di) = device.GetDeviceIdentification()
    assert r.ReturnCode == 1
    logging.debug(di.DeviceName + " " + di.DeviceSerialNumber + " " + di.DeviceFirmwareVersion + " " + di.DeviceManufacturer + " " + di.Wsdl + " " + str(di.SiLADeviceClass))
    return di 

def OnStatusEvent(sea: StatusEventArgsWrapper):
    assert sea is not None
    print(sea.EventDescription.Classification + " received from " + sea.Device.DeviceName + ": ")
    #print(str(sea.ReturnValue.ReturnCode) + " " + sea.ReturnValue.Message.split("\r\n", 1)[0] + " (Code " + str(sea.InternalErrorCode) + " " + sea.EventDescription.Raw + ")")
    print(str(sea.ReturnValue.ReturnCode) + " " + sea.EventDescription.StatusMessage + " (Code " + str(sea.EventDescription.InternalCode) + " " + sea.EventDescription.InternalCodeName + " " + sea.EventDescription.InternalCodeDescription + ")")
    print("Correction hint: " + sea.EventDescription.FaultCorrectionsHints)

if config['IHC']['ODTC'] == "True":
    def OnDataEvent(dataEventSensorValues: List[DataEventOdtcSensorValue]):
        #val: DataEventOdtcSensorValue
        for val in dataEventSensorValues:
            print(val)
        print("OnDataEvent called")

if config['IHC']['ODTC'] == "True":
    def PollRAT(odtc: OdtcWrapper, iterations = 5):
        assert odtc != None
        i = 0
        while i < iterations:
            rv = odtc.ReadActualTemperature()
            assert rv.Success == True
            at = rv.ResponseData.SensorValues
            print("Async Polling RAT - Mount: " + str(at.Mount / 100))
            time.sleep(1)
            i += 1
        # Test SubStates (parallel command processing)
        di = GetStatus(odtc)
        for value in di.SubStates:
            print("SubStates: " + value.CommandName + " " + str(value.RequestId) + " " + value.CurrentState + " " + str(value.QueuePosition) + " " + value.StartedAt)
        print("StopMethod (from PollRAT)")
        res = odtc.StopMethod()
        assert res.Success == True

if config['IHC']['ODTC'] == "True":
    def DownloadOdtcLogTraces(ip: str, path: str, traceFileCount: int, logs: bool = True, legacy: bool = False):
        assert ip != None
        assert path != None
        downloader = OdtcDownloaderWrapper()
        if logs:
            if legacy:
                # Download device logs
                items = downloader.GetItems(ip, "Logs")
                for item in items:
                    if item.Value != "InhecoSiLA.log":
                        item.Download = True
                error = downloader.DownloadFtpItems(items, path)
                if error is not None:
                    return error
            else:
                # Download SiLA logs
                items = downloader.GetItems(ip, "SiLA")
                for item in items:
                    item.Download = True
                error = downloader.DownloadFtpItems(items, path)
                if error is not None:
                   return error
                # Download device logs
                items = downloader.GetItems(ip, "Odtc")
                for item in items:
                    item.Download = True
                error = downloader.DownloadFtpItems(items, path)
                if error is not None:
                    return error
        # Download traces files
        if traceFileCount == 0:
            return None
        items = downloader.GetItems(ip, "Traces")
        traces = [x for x in items if x.IsTrace == True]
        def TakeValue(item):
            return item.Value
        traces.sort(key=TakeValue, reverse=True)
        for idx, x in enumerate(traces):
            if idx < traceFileCount or traceFileCount < 0:
                traces[idx].Download = True
            else:
                break
        return downloader.DownloadFtpItems(traces, path)

if config['IHC']['SCILA'] == "True":
    def DownloadScilaLogTraces(ip: str, path: str, traceFileCount: int, logs: bool = True) -> str:
        assert ip != None
        assert path != None
        downloader = ScilaDownloaderWrapper()
        if logs:
            # Download SiLA logs
            items = downloader.GetItems(ip, "SiLA")
            for item in items:
                item.Download = True
            error = downloader.DownloadFtpItems(items, path)
            if error is not None:
                return error
            # Download device logs
            items = downloader.GetItems(ip, "Scila/Logs")
            for item in items:
                item.Download = True
            error = downloader.DownloadFtpItems(items, path)
            if error is not None:
                return error
        # Download traces files
        if traceFileCount == 0:
            return None
        items = downloader.GetItems(ip, "Scila/Traces")
        traces = [x for x in items if x.IsTrace == True]
        def TakeNumber(item: FtpItemWrapper):
            return int(item.Value[7: item.Value.index(".")])
        traces.sort(key=TakeNumber, reverse=True)
        for idx, x in enumerate(traces):
            if idx < traceFileCount or traceFileCount < 0:
                traces[idx].Download = True
            else:
                break
        return downloader.DownloadFtpItems(traces, path)

if __name__ == "__main__":
    main()
