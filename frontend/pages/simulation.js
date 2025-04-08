import { useState } from 'react';

export default function Simulation() {
  const [result, setResult] = useState('');

  const runSimulation = async (scenario) => {
    const res = await fetch(`/api/simulation/${scenario}`, { method: 'POST' });
    const data = await res.json();
    setResult(data.result);
  };

  return (
    <div>
      <h2>Stock Simulation</h2>
      <button onClick={() => runSimulation('bull')}>Run Bull Market Simulation</button>
      <button onClick={() => runSimulation('bear')}>Run Bear Market Simulation</button>
      <button onClick={() => runSimulation('volatile')}>Run Volatile Market Simulation</button>
      {result && <p>Result: {result}</p>}
    </div>
  );
}
