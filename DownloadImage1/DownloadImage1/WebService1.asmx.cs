using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Web;
using System.Web.Services;

namespace DownloadImage1
{
    /// <summary>
    /// Summary description for WebService1
    /// </summary>
    [WebService(Namespace = "http://tempuri.org/")]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    [System.ComponentModel.ToolboxItem(false)]
    // To allow this Web Service to be called from script, using ASP.NET AJAX, uncomment the following line. 
    // [System.Web.Script.Services.ScriptService]
    public class WebService1 : System.Web.Services.WebService
    {

        [WebMethod]
        public string HelloWorld()
        {
            return "Hello World";
        }
        [WebMethod, Description("Get Image Content")]
        public byte[] GetImageFile(string fileName)
        {
            if (System.IO.File.Exists(Server.MapPath("~/Images/") + fileName))
            {
                return System.IO.File.ReadAllBytes(Server.MapPath("~/Images/") + fileName);

            }
            else {
                return new byte[] { 0};
            }
        }

    }
}
