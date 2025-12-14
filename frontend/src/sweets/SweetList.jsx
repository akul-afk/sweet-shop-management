import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/axios";

export default function SweetList() {
  const [sweets, setSweets] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("token");

    // 🔒 If not logged in, redirect immediately
    if (!token) {
      navigate("/login");
      return;
    }

    // ✅ Only call API if token exists
    api.get("/api/sweets")
      .then((res) => setSweets(res.data))
      .catch((err) => {
        if (err.response?.status === 401) {
          localStorage.removeItem("token");
          navigate("/login");
        }
      });
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
