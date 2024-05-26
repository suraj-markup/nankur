import React from "react";
import ReactDOM from "react-dom/client"; 
import Header from "./components/Header.js";
import Body from "./components/Body.js";
import About from "./components/About.js";
import Contact from "./components/Contact.js";
import Error from "./components/Error.js";
import RestaurantMenu from "./components/RestaurantMenu.js";
import { createBrowserRouter,RouterProvider,Outlet } from "react-router-dom";

const AppLayout = ()=>{
  
  return (
    <div className="p-5 bg-orange-50 h-auto">
      <Header/>
      <Outlet/>
    </div>

  )
}

const appRouter= createBrowserRouter([
  {
    path: "/",
    element:<AppLayout/>,
    children:[
        {
          path: "/",
          element:<Body/>
      
        },
        {
        path: "/about",
        element:<About/>
    
        },
        {
          path: "/contact",
          element:<Contact/>,
      
        },
        {
          path: "/restaurants/:resId",
          element:<RestaurantMenu/>,
      
        },
    ], 
    errorElement:<Error/>

  },
  
  
]);

const root=ReactDOM.createRoot(document.getElementById("root"));

root.render(<RouterProvider router={appRouter}/>);