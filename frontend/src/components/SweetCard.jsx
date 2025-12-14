export default function SweetCard({ sweet, onPurchase }) {
  const out = sweet.quantity === 0;

  return (
    <div className="card">
      <div className="card-img">
        <i className="fas fa-cookie"></i>
      </div>

      <div className="card-body">
        <div className="card-category">{sweet.category}</div>
        <h3 className="card-title">{sweet.name}</h3>

        <div className="card-meta">
          <span className="price">₹{sweet.price}</span>
          <span className={`stock ${out ? "out" : ""}`}>
            {out ? "Out of Stock" : `${sweet.quantity} left`}
          </span>
        </div>

        <button
          className="btn btn-purchase"
          disabled={out}
          onClick={() => onPurchase(sweet.id)}
        >
          {out ? "Unavailable" : "Purchase"}
        </button>
      </div>
    </div>
  );
}
