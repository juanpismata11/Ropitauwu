import React from "react";
import './Inputs.css'

interface InputsProps {
  nombre: string;
  tipo: string;
  valor: string;
}

const Inputs: React.FC<InputsProps> = ({ nombre, tipo, valor }) => {
  return(
    <div className="input-container">
      <label className="input-label">{nombre}</label>
      <input id={valor} type={tipo}/>
    </div>
  );
};

export default Inputs;