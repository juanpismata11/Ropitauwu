import React, { useRef, useState} from 'react';
import './RopaContainer.css';
import { IonImg } from '@ionic/react';


interface ContainerProps {
  img: string;
}

const RopaContainer: React.FC<ContainerProps> = ({ img }) => {
  const cargarImagen = useRef<HTMLInputElement>(null);
  const [selectedImage, setSelectedImage] = useState<string | null>(null);

  const HandleSeleccionarImagen = () => {
    cargarImagen.current?.click();
  }

  const handleCambioImagen = (event: React.ChangeEvent<HTMLInputElement>) => {
    try {
      const archivo = event.target.files?.[0];
      if (archivo) {
        const url = URL.createObjectURL(archivo);
        setSelectedImage(url);
      }


    } catch (error) {
      console.error("Error al cargar la imagen:", error);
    }
    
  };
  

  return (
    <div className="container">
      <button className="botonAdd" onClick={HandleSeleccionarImagen}>{img}</button>
      <input
        type="file"
        accept="image/*"
        ref={cargarImagen}
        onChange={handleCambioImagen}
        style={{ display: 'none' }}
      />

      {selectedImage && (
        <IonImg src={selectedImage} style={{ marginTop: '20px', width: '200px' }} />
      )}
    </div>

    
  );
};

export default RopaContainer;
