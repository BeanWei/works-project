<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="12008004">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="IOScan.Faults" Type="Str"></Property>
		<Property Name="IOScan.NetVarPeriod" Type="UInt">100</Property>
		<Property Name="IOScan.NetWatchdogEnabled" Type="Bool">false</Property>
		<Property Name="IOScan.Period" Type="UInt">10000</Property>
		<Property Name="IOScan.PowerupMode" Type="UInt">0</Property>
		<Property Name="IOScan.Priority" Type="UInt">9</Property>
		<Property Name="IOScan.ReportModeConflict" Type="Bool">true</Property>
		<Property Name="IOScan.StartEngineOnDeploy" Type="Bool">false</Property>
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="SubVI" Type="Folder">
			<Item Name="_jki_lib_state_machine" Type="Folder">
				<Item Name="Add State(s) to Queue__jki_lib_state_machine.vi" Type="VI" URL="../SubVI/_jki_lib_state_machine.llb/Add State(s) to Queue__jki_lib_state_machine.vi"/>
				<Item Name="Build State String with Arguments__jki_lib_state_machine.vi" Type="VI" URL="../SubVI/_jki_lib_state_machine.llb/Build State String with Arguments__jki_lib_state_machine.vi"/>
				<Item Name="Parse State Queue__jki_lib_state_machine.vi" Type="VI" URL="../SubVI/_jki_lib_state_machine.llb/Parse State Queue__jki_lib_state_machine.vi"/>
				<Item Name="String-Based Queued State Machine (Basic 1.0)__jki_lib_state_machine.vi" Type="VI" URL="../SubVI/_jki_lib_state_machine.llb/String-Based Queued State Machine (Basic 1.0)__jki_lib_state_machine.vi"/>
				<Item Name="VI Tree - JKI State Machine__jki_lib_state_machine.vi" Type="VI" URL="../SubVI/_jki_lib_state_machine.llb/VI Tree - JKI State Machine__jki_lib_state_machine.vi"/>
			</Item>
			<Item Name="Add Item.vi" Type="VI" URL="../SubVI/Add Item.vi"/>
			<Item Name="Directory to Tree.vi" Type="VI" URL="../SubVI/Directory to Tree.vi"/>
			<Item Name="Emergency ahort VIs.vi" Type="VI" URL="../SubVI/Emergency ahort VIs.vi"/>
			<Item Name="Init_Open_Close.vi" Type="VI" URL="../SubVI/Init_Open_Close.vi"/>
			<Item Name="Initialize.vi" Type="VI" URL="../SubVI/Initialize.vi"/>
			<Item Name="MultiFileGraphChoose.vi" Type="VI" URL="../SubVI/MultiFileGraphChoose.vi"/>
			<Item Name="ReadFromMultiFile.vi" Type="VI" URL="../SubVI/ReadFromMultiFile.vi"/>
			<Item Name="ReadFromSIngelFile.vi" Type="VI" URL="../SubVI/ReadFromSIngelFile.vi"/>
			<Item Name="SingleFileGraphChoose.vi" Type="VI" URL="../SubVI/SingleFileGraphChoose.vi"/>
			<Item Name="Validate.vi" Type="VI" URL="../SubVI/Validate.vi"/>
			<Item Name="删除无效的文件路径.vi" Type="VI" URL="../SubVI/删除无效的文件路径.vi"/>
		</Item>
		<Item Name="DataAnalysis.vi" Type="VI" URL="../DataAnalysis.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="General Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler.vi"/>
				<Item Name="LVPoint32TypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVPoint32TypeDef.ctl"/>
				<Item Name="LVRectTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVRectTypeDef.ctl"/>
				<Item Name="Read From Spreadsheet File (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read From Spreadsheet File (DBL).vi"/>
				<Item Name="Read From Spreadsheet File (I64).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read From Spreadsheet File (I64).vi"/>
				<Item Name="Read From Spreadsheet File (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read From Spreadsheet File (string).vi"/>
				<Item Name="Read From Spreadsheet File.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read From Spreadsheet File.vi"/>
				<Item Name="Set Busy.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/cursorutil.llb/Set Busy.vi"/>
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="Unset Busy.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/cursorutil.llb/Unset Busy.vi"/>
			</Item>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
