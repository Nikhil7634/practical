using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace DownloadImage1
{
    public partial class DownloadImage : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            Image1.ImageUrl = "~/MyHandler.ashx?fileName=" +txt1.Text;
            Response.Write("Downloading of Image is Done");
        }
    }
}