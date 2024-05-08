using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace DownloadImage1
{
    /// <summary>
    /// Summary description for MyHandler
    /// </summary>
    public class MyHandler : IHttpHandler
    {

        public void ProcessRequest(HttpContext context)
        {
            WebService1 img = new WebService1();
            byte[] binImage = img.GetImageFile(context.Request["fileName"]);
            if (binImage.Length == 1)
            { 
            
            }
            else
            {
                context.Response.ContentType="image/jpeg";
                context.Response.BinaryWrite(binImage);
            }
        }

        public bool IsReusable
        {
            get
            {
                return false;
            }
        }
    }
}