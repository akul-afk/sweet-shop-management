export default function Shop() {
  return (
    <div className="container">
      <section style={{ textAlign: "center", marginBottom: "3rem" }}>
        <h1>Freshly Baked Happiness</h1>
        <p>Order online and get it delivered in minutes.</p>
      </section>

      {/* Search + Filter */}
      <div className="controls">
        <div className="search-bar">
          <i className="fas fa-search"></i>
          <input placeholder="Search for donuts, cookies..." />
        </div>

        <select className="category-filter">
          <option>All Categories</option>
          <option>Donuts</option>
          <option>Cookies</option>
          <option>Cakes</option>
        </select>
      </div>

      {/* Product Grid */}
      <div className="grid">
  <ProductCard name="Glazed Donut" price={2.5} qty={15} category="donuts" />
  <ProductCard name="Choco Chip Cookie" price={1.8} qty={0} category="cookies" />
  <ProductCard name="Red Velvet Cake" price={25} qty={5} category="cakes" />
</div>

    </div>
  );
}

function ProductCard({ name, price, qty, category }) {
  return (
    <div className="card">
      <div className={`card-img ${category}`}></div>

      <div className="card-body">
        <div className="card-category">{category.toUpperCase()}</div>
        <h3>{name}</h3>

        <div className="card-meta">
          <span className="price">${price.toFixed(2)}</span>
          <span className="stock">{qty} left</span>
        </div>

        <button className="btn">Purchase</button>
      </div>
    </div>
  );
}
