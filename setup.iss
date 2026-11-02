
[Setup]
AppName=My Calculator
AppVersion=1.0
DefaultDirName={localappdata}\Programs\My Calculator
DefaultGroupName=My Calculator
OutputDir=installer
OutputBaseFilename=MyCalculator_Setup
Compression=lzma
SolidCompression=yes
PrivilegesRequired=lowest
UninstallDisplayIcon={app}\MyCalculator.exe

[Files]
Source: "dist\MyCalculator.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\My Calculator"; Filename: "{app}\MyCalculator.exe"
Name: "{autodesktop}\My Calculator"; Filename: "{app}\MyCalculator.exe"

[Run]
Filename: "{app}\MyCalculator.exe"; Description: "Launch My Calculator"; Flags: nowait postinstall skipifsilent
