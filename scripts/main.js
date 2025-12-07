/* Reset y estilos base */
* {
  margin: 0;
  padding: 0;
  box- sizing: border - box;
}

html {
  scroll - behavior: smooth;
}

body {
  font - family: 'Segoe UI', Tahoma, Geneva, Verdana, sans - serif;
  line - height: 1.6;
  color: #333;
  overflow - x: hidden;
}

/* Tipografía */
h1, h2, h3, h4, h5, h6 {
  font - weight: 700;
  line - height: 1.2;
}

/* Utilidades */
.container {
  width: 100 %;
  max - width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Animaciones */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.fade -in {
  animation: fadeIn 0.8s ease- out;
}

/* Responsive Images */
img {
  max - width: 100 %;
  height: auto;
}

/* Ajustes de accesibilidad */
@media(prefers - reduced - motion: reduce) {
  * {
    animation- duration: 0.01ms!important;
  animation - iteration - count: 1!important;
  transition - duration: 0.01ms!important;
}

  html {
  scroll - behavior: auto;
}
}

/* Utilidades de texto */
.text - center {
  text - align: center;
}

.text - primary {
  color: #0066cc;
}

/* Botones */
.btn {
  display: inline - block;
  padding: 12px 24px;
  border - radius: 50px;
  text - decoration: none;
  font - weight: 600;
  font - size: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
}

.btn:hover {
  transform: translateY(-2px);
  box - shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

/* Grid system básico */
.row {
  display: flex;
  flex - wrap: wrap;
  margin: 0 - 15px;
}

.col {
  flex: 1;
  padding: 0 15px;
}

/* Loading states */
.loading {
  opacity: 0.7;
  pointer - events: none;
}

/* Focus styles para accesibilidad */
:focus {
  outline: 2px solid #0066cc;
  outline - offset: 2px;
}

: focus: not(: focus - visible) {
  outline: none;
}

/* Scrollbar personalizada */
:: -webkit - scrollbar {
  width: 10px;
}

:: -webkit - scrollbar - track {
  background: #f1f1f1;
}

:: -webkit - scrollbar - thumb {
  background: #888;
  border - radius: 5px;
}

:: -webkit - scrollbar - thumb:hover {
  background: #555;
}

/* Media queries responsive */
@media(max - width: 768px) {
  .container {
    padding: 0 15px;
  }

  h1 {
    font - size: 2rem;
  }

  h2 {
    font - size: 1.75rem;
  }

  h3 {
    font - size: 1.5rem;
  }
}