#NoTrayIcon
Opt("TrayIconHide", 1)
Opt("TrayMenuMode", 3)

#include <AutoItConstants.au3>
#include <MsgBoxConstants.au3>
#include <TrayConstants.au3>
#include <WinAPIProc.au3>

Local $title = "Hotspot@UPM Auto Login Laucher"
Local $hMain
Local $state

_WinAPI_CreateMutex($title)
Local $err = _WinAPI_GetLastError()
if ($err == 183) Then
   MsgBox(48, $title, $title & " already running!")
   Exit
EndIf

Func tray_clicked()
   $state = WinGetState($hMain)
   if $state == 15 or $state == 7 Then
	  WinSetState($hMain,"",@SW_HIDE)
   ElseIf $state == 5 or $state == 21 Then
	  WinSetState($hMain,"",@SW_RESTORE)
	  WinActivate($hMain)
   EndIf
   Return 0
EndFunc

TraySetState($TRAY_ICONSTATE_HIDE)
TraySetIcon("res\icon.ico")
TraySetToolTip($title)

; TRAY MENU
Local $tSH = TrayCreateItem("Show/Hide")
TrayCreateItem("")
Local $tExit = TrayCreateItem("Exit")

Run("hotspot.exe","", @SW_HIDE)

Do
   Sleep(250)
   $hMain = WinGetHandle("[TITLE:Hotspot@UPM Auto Login;CLASS:TkTopLevel]")
Until $hMain > 0

TraySetOnEvent ( $TRAY_EVENT_PRIMARYDOUBLE, "tray_clicked" )
TraySetState($TRAY_ICONSTATE_SHOW)

While 1
   Switch TrayGetMsg()
   Case $tExit
	  WinClose($hMain)
	  Exit
   Case $tSH
	  tray_clicked()
   Case $TRAY_EVENT_PRIMARYDOUBLE
	  tray_clicked()
   Case Else
	  $state = WinGetState($hMain)
	  if $state == 23 Then
		 WinSetState($hMain,"",@SW_HIDE)
	  ElseIf $state == 0 Then
		 WinClose($hMain)
		 Exit
	  EndIf
   EndSwitch
WEnd