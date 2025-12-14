import { useState } from "react";
import { useAuth } from "../auth/AuthContext";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const { login } = useAuth();
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("user");

  const submit = async (e) => {
    e.preventDefault();
    await login(email, password, role);
    navigate("/shop");
  };

  return (
    <form onSubmit={submit} className="auth-form">
      <h2>Login</h2>

      <div className="role-toggle">
        <button type="button" onClick={() => setRole("user")}>
          User
        </button>
        <button type="button" onClick={() => setRole("admin")}>
          Admin
        </button>
      </div>

      <input placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
      <input
        type="password"
        placeholder="Password"
        onChange={(e) => setPassword(e.target.value)}
      />

      <button className="btn">Login</button>
    </form>
  );
}
