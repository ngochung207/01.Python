Sub HocVBA()
    '// add declarations
    Dim arr()
    
    On Error GoTo catchError
exitSub:
    Exit Sub
catchError:
    '// add error handling
    GoTo exitSub
End Sub