<%-- 
    Document   : output
    Created on : 6 May, 2024, 11:29:23 PM
    Author     : sumed
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
            <%-- start web service invocation --%><hr/>
    <%
    try {
	Client.Currency_Service service = new Client.Currency_Service();
	Client.Currency port = service.getCurrencyPort();
	 // TODO initialize WS operation arguments here
	double a = Double.parseDouble(request.getParameter("t1"));
	// TODO process result here
	java.lang.String result = port.inrtoDollr(a);
	out.println(result);
    } catch (Exception ex) {
	// TODO handle custom exceptions here
    }
    %>
    <%-- end web service invocation --%><hr/>

    </body>
</html>
