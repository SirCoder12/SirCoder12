vb
Imports System

Module HelloWorld
    Sub Main()
        Console.WriteLine("Please enter your name:")
        Dim name As String = Console.ReadLine()
        Console.WriteLine("Hello, " & name & "! Welcome to Visual Basic.")
        Console.ReadLine()
    End Sub
End Module