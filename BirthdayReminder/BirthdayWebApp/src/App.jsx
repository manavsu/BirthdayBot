import React, {useState, useEffect} from "react";
import Loading from "./Components/LoadingComponent.jsx";
import GetBirthdayData from "./Utils/GetBirthdayData.jsx";
import BirthdayRow from "./Components/BirthdayRowComponent.jsx";
import "./Styles/Global.css"

function App() {
    const [birthdays, setBirthdays] = useState(null);
    useEffect(() => {
        GetBirthdayData(setBirthdays);
    }, []);
    console.log(birthdays);
    if (!birthdays) return <Loading />;
    const fbirthdays = birthdays.map((b) => <BirthdayRow birthday={b}/>)
    return (
      <>
        <table><tbody>{fbirthdays}</tbody></table>
      </>
    );
}

export default App
