export async function fetchAPI(endpoint, options) {
    const res = await fetch(endpoint, options);
    return res.json();
  }
  