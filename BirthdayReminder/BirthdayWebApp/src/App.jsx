import React, { useState, useEffect } from "react";
import Loading from "./Components/LoadingComponent.jsx";
import {GetBirthdayData, DeleteBirthdayAndReload} from "./APIUtils/APICalls.jsx";
import {BirthdayRow, BirthdayRowHeader, AddRow}from "./Components/BirthdayRowComponent.jsx";
import "./Styles/Global.css";

function App() {
  const [birthdays, setBirthdays] = useState(null);
  useEffect(() => GetBirthdayData(setBirthdays), []);
  if (!birthdays) return <Loading />;

  const birthdayRows = birthdays.map((b) => <li><BirthdayRow birthday={b} onDelete={(name) => DeleteBirthdayAndReload(name, setBirthdays)}/></li>);

  return (
    <>
      <ul>
        <BirthdayRowHeader />
        {birthdayRows}
        <AddRow />
      </ul>
    </>
  );
}

export default App;
