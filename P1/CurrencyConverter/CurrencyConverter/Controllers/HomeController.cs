using Microsoft.AspNetCore.Mvc;

namespace CurrencyConverter.Controllers
{
    public class HomeController : Controller
    {
        public ActionResult Index()
        {
            return View();
        }

        public ActionResult Convert(string currency,decimal amount)
        {
            decimal result = 0;
            decimal conversionRate = 0;

            if(currency == "INRtoUSD")
            {
                conversionRate = 0.013m ;
            }
            else if(currency == "USDtoINR")
            {
                conversionRate = 74.50m;
            }
            result = (amount * conversionRate);
            ViewBag.Result = result;
            return View("Index");
        }
    }
}
