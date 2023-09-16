import Form from "./Form"
function Home(){
  return (
    <div className="page">
        <div id= "head" className="header bg-orange-500">
            <image href = ""> </image>
        </div>
        <div id="body" className="backdrop-blur-sm md:backdrop-blur-lg bg-[/Users/harakala/Code/vthacks23/frontend/VTHacks23/src/img/backdrop.jpg]">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </div>
        <div id="foot">

        </div>
        <Form/>
    </div>
    
  )
}

export default Home