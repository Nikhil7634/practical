/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package StringOperationSPackage;

import javax.ws.rs.core.Context;
import javax.ws.rs.core.UriInfo;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PUT;

/**
 * REST Web Service
 *
 * @author student
 */
@Path("generic")
public class Stringoperations {

    @Context
    private UriInfo context;

    /**
     * Creates a new instance of Stringoperations
     */
    public Stringoperations() {
    }

    /**
     * Retrieves representation of an instance of StringOperationSPackage.Stringoperations
     * @return an instance of java.lang.String
     */
    @GET
    @Produces("text/html")
    public String getHtml() {
        //TODO return proper representation object
        throw new UnsupportedOperationException();
    }

    /**
     * PUT method for updating or creating an instance of Stringoperations
     * @param content representation for the resource
     * @return an HTTP response with content of the updated or created resource.
     */
    @PUT
    @Consumes("text/html")
    
    public void putHtml(String content) {
    }
    @PUT
    @Consumes("text/html")
    @Path("/Uppercase")
    public String toUppercasMethod(String str)
    {
        return str.toUpperCase();
    }
    @PUT
    @Consumes("text/html")
    @Path("/Lowercase")
    public String toLowercaseMethod(String str)
    {
        return str.toUpperCase();
    }
}
