import React from "react";

function BirthdayRow({ birthday }) {
  console.log(birthday);
  return (
    <tr className="birthday">
      <td>{birthday.name}</td>
      <td>
        {birthday.date.month} / {birthday.date.day}
      </td>
    </tr>
  );
}

export default BirthdayRow;
