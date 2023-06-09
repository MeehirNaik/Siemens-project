# Siemens-project
all files


Imports System.Drawing
Imports System.Windows.Forms
Imports AForge.Video
Imports AForge.Video.DirectShow

Public Class MainForm
    Inherits Form

    Private videoPlayer As New PictureBox()
    Private videoSource As VideoCaptureDevice

    Public Sub New()
        InitializeComponent()
        InitializeCamera()
    End Sub

    Private Sub InitializeComponent()
        Me.SuspendLayout()

        ' MainForm properties
        Me.ClientSize = New Size(640, 480)
        Me.Text = "Camera App"

        ' videoPlayer properties
        Me.videoPlayer.Size = Me.ClientSize
        Me.videoPlayer.SizeMode = PictureBoxSizeMode.StretchImage

        ' Add videoPlayer to MainForm
        Me.Controls.Add(Me.videoPlayer)

        Me.ResumeLayout(False)
    End Sub

    Private Sub InitializeCamera()
        Dim videoDevices As FilterInfoCollection = New FilterInfoCollection(FilterCategory.VideoInputDevice)
        If videoDevices.Count > 0 Then
            videoSource = New VideoCaptureDevice(videoDevices(0).MonikerString)
            AddHandler videoSource.NewFrame, AddressOf VideoSource_NewFrame
            videoSource.Start()
        Else
            MessageBox.Show("No video devices found.")
        End If
    End Sub

    Private Sub VideoSource_NewFrame(sender As Object, eventArgs As NewFrameEventArgs)
        videoPlayer.Image = DirectCast(eventArgs.Frame.Clone(), Bitmap)
    End Sub

    Protected Overrides Sub OnClosed(e As EventArgs)
        MyBase.OnClosed(e)
        videoSource.SignalToStop()
        videoSource.WaitForStop()
    End Sub

    Public Shared Sub Main()
        Application.Run(New MainForm())
    End Sub
End Class

