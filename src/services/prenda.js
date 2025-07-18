
async function getPrendaService(){
  try {
    const response = await fetch('http://localhost:8000/prendas')
    
    if(!response.ok){
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const prendas = await response.json();
    return prendas;

  } catch (error) {
    console.error("Error fetching prendas:", error);
    throw error;
  }
}