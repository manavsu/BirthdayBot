import React, { useState, useEffect } from "react";
import Loading from "./Components/LoadingComponent.jsx";
import GetBirthdayData from "./Utils/GetBirthdayData.jsx";
import BirthdayRow from "./Components/BirthdayRowComponent.jsx";
import "./Styles/Global.css";

function App() {
  const [birthdays, setBirthdays] = useState(null);
  useEffect(() => GetBirthdayData(setBirthdays), []);
  if (!birthdays) return <Loading />;

  const birthdayRows = birthdays.map((b) => <BirthdayRow birthday={b} />);

  return (
    <>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>{birthdayRows}</tbody>
      </table>
    </>
  );
}

export default App;
