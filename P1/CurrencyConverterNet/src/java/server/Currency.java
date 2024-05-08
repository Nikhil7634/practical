/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package server;

import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.jws.WebParam;

/**
 *
 * @author sumed
 */
@WebService(serviceName = "Currency")
public class Currency {

    /**
     * This is a sample web service operation
     */
    @WebMethod(operationName = "hello")
    public String hello(@WebParam(name = "name") String txt) {
        return "Hello " + txt + " !";
    }

    /**
     * Web service operation
     */
    @WebMethod(operationName = "InrtoDollr")
    public String InrtoDollr(@WebParam(name = "a") double a) {
        //TODO write your implementation code here:
        return "The Indian rupees" + a + "in Dollars is" + (a/83.17);
    }
}
