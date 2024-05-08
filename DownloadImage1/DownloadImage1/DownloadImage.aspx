<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="DownloadImage.aspx.cs" Inherits="DownloadImage1.DownloadImage" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <center>
            <asp:Label ID="Label1" runat="server" Text="Enter the name of image to download and show" BorderStyle="Ridge"></asp:Label>
            <asp:TextBox ID="txt1" runat="server" BorderStyle="Groove"></asp:TextBox>
            <br />
            <br />
            <asp:Button ID="Button1" runat="server" BorderStyle="Ridge" OnClick="Button1_Click" Text="Download Image and Show" />
            <br />
            <br />
            <asp:Image ID="Image1" runat="server" />
            <br />
        </center>
    </form>
</body>
</html>
