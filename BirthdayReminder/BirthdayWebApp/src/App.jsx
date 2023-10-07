import React, {useState, useEffect} from "react";
import GetBirthdayData from "./Utils/GetBirthdayData.jsx";
import Loading from "./Components/LoadingComponent.jsx";
import "./styles/Global.css";

function App () {
    const [birthdays, setBirthdays] = useState(null);
    // useEffect(() => {
    //     GetBirthdayData(setBirthdays);
    // }, []);

    if (!birthdays) return <Loading />;
    console.log(birthdays);
    return (
      <h1>found</h1>
    );
}

export default App;

