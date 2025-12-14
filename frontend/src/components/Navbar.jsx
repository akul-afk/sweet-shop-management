import { Link } from "react-router-dom";
import { useAuth } from "../auth/AuthContext";

export default function Navbar() {
  const { token, logout } = useAuth();

  return (
    <nav style={styles.nav}>
      <div style={styles.brand}>
        🍪 <span>Sugarsnap</span>
      </div>

      <div style={styles.links}>
        <Link to="/">Shop</Link>

        {!token && <Link to="/login">Login</Link>}
        {!token && <Link to="/register">Register</Link>}

        {token && <Link to="/admin">Admin</Link>}
        {token && (
          <button onClick={logout} style={styles.logout}>
            Logout
          </button>
        )}
      </div>
    </nav>
  );
}

const styles = {
  nav: {
    background: "#fff",
    padding: "1rem 2rem",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    boxShadow: "0 4px 10px rgba(0,0,0,0.05)"
  },
  brand: {
    fontWeight: "800",
    fontSize: "1.2rem",
    color: "#ff6b81"
  },
  links: {
    display: "flex",
    gap: "1.5rem",
    alignItems: "center"
  },
  logout: {
    border: "none",
    background: "#ff6b81",
    color: "#fff",
    padding: "0.4rem 0.8rem",
    borderRadius: "8px",
    cursor: "pointer"
  }
};
