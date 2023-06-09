# Siemens-project
all files


Imports System.Drawing
Imports System.Windows.Forms
Imports AForge.Video
Imports AForge.Video.DirectShow

Public Class MainForm
    Inherits Form

    Private videoPlayer As New PictureBox()
    Private captureButton As New Button()
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

        ' captureButton properties
        Me.captureButton.Text = "Capture"
        Me.captureButton.Size = New Size(80, 30)
        Me.captureButton.Location = New Point((Me.ClientSize.Width - Me.captureButton.Width) \ 2, Me.ClientSize.Height - 50)
        Me.captureButton.Anchor = AnchorStyles.Bottom Or AnchorStyles.Left Or AnchorStyles.Right

        ' Add controls to MainForm
        Me.Controls.Add(Me.videoPlayer)
        Me.Controls.Add(Me.captureButton)

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

    Private Sub CaptureButton_Click(sender As Object, e As EventArgs) Handles captureButton.Click
        Dim captureImage As Image = videoPlayer.Image
        If captureImage IsNot Nothing Then
            captureImage.Save("captured_image.jpg", Imaging.ImageFormat.Jpeg)
            MessageBox.Show("Image captured and saved as captured_image.jpg")
        End If
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
