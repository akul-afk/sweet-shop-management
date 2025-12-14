import { useEffect, useState } from "react";
import api from "../api/axios";

export default function SweetList() {
  const [sweets, setSweets] = useState([]);

  useEffect(() => {
    api.get("/api/sweets").then((res) => setSweets(res.data));
  }, []);

  const purchase = async (id) => {
    await api.post(`/api/sweets/${id}/purchase`);
    setSweets((prev) =>
      prev.map((s) =>
        s.id === id ? { ...s, quantity: s.quantity - 1 } : s
      )
    );
  };

  return (
    <>
      <h2>Sweets</h2>
      {sweets.map((s) => (
        <div key={s.id}>
          <b>{s.name}</b> – ₹{s.price} – Qty: {s.quantity}
          <button disabled={s.quantity === 0} onClick={() => purchase(s.id)}>
            Buy
          </button>
        </div>
      ))}
    </>
  );
}
