import { useEffect, useState } from "react";
import api from "../api/axios";

export default function Admin() {
  const [sweets, setSweets] = useState([]);

  useEffect(() => {
    api.get("/api/sweets").then((res) => setSweets(res.data));
  }, []);

  const remove = async (id) => {
    await api.delete(`/api/sweets/${id}`);
    setSweets(sweets.filter((s) => s.id !== id));
  };

  return (
    <div className="container">
      <h2>Manage Inventory</h2>

      <table className="sweet-table">
        <thead>
          <tr>
            <th>Name</th>
            <th>Category</th>
            <th>Price</th>
            <th>Qty</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {sweets.map((s) => (
            <tr key={s.id}>
              <td>{s.name}</td>
              <td>{s.category}</td>
              <td>₹{s.price}</td>
              <td>{s.quantity}</td>
              <td>
                <button className="action-btn delete-btn" onClick={() => remove(s.id)}>
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
