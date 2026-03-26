import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

const API_URL = "http://127.0.0.1:8000";

function App() {
  const [form, setForm] = useState({
    name: "",
    email: "",
    subject: "",
    message: "",
  });

  const [contacts, setContacts] = useState([]);
  const [editingId, setEditingId] = useState(null);
  const [mensaje, setMensaje] = useState("");
  const [loading, setLoading] = useState(false);

  const loadContacts = async () => {
    try {
      const response = await axios.get(`${API_URL}/contacts`);
      setContacts(response.data);
    } catch (error) {
      console.error("Error cargando contactos:", error);
    }
  };

  useEffect(() => {
    loadContacts();
  }, []);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const resetForm = () => {
    setForm({
      name: "",
      email: "",
      subject: "",
      message: "",
    });
    setEditingId(null);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setMensaje("");

    try {
      if (editingId) {
        await axios.put(`${API_URL}/contacts/${editingId}`, form);
        setMensaje("Contacto actualizado correctamente");
      } else {
        await axios.post(`${API_URL}/contacts`, form);
        setMensaje("Contacto enviado correctamente");
      }

      resetForm();
      loadContacts();
    } catch (error) {
      console.error(error);
      setMensaje("Error al procesar el contacto");
    } finally {
      setLoading(false);
    }
  };

  const handleEdit = (contact) => {
    setForm({
      name: contact.name,
      email: contact.email,
      subject: contact.subject,
      message: contact.message,
    });
    setEditingId(contact.id);
    setMensaje("");
  };

  const handleDelete = async (id) => {
    try {
      await axios.delete(`${API_URL}/contacts/${id}`);
      setMensaje("Contacto eliminado correctamente");
      if (editingId === id) {
        resetForm();
      }
      loadContacts();
    } catch (error) {
      console.error(error);
      setMensaje("Error al eliminar el contacto");
    }
  };

  return (
    <div style={{ maxWidth: "900px", margin: "auto", padding: "20px" }}>
      <h2>Formulario de Contacto</h2>

      <form onSubmit={handleSubmit} style={{ marginBottom: "30px" }}>
        <input
          type="text"
          name="name"
          placeholder="Nombre"
          value={form.name}
          onChange={handleChange}
          required
        />

        <input
          type="email"
          name="email"
          placeholder="Correo"
          value={form.email}
          onChange={handleChange}
          required
        />

        <input
          type="text"
          name="subject"
          placeholder="Asunto"
          value={form.subject}
          onChange={handleChange}
          required
        />

        <textarea
          name="message"
          placeholder="Mensaje"
          value={form.message}
          onChange={handleChange}
          required
        />

        <button type="submit" disabled={loading}>
          {loading ? "Procesando..." : editingId ? "Actualizar" : "Enviar"}
        </button>

        {editingId && (
          <button type="button" onClick={resetForm} style={{ marginLeft: "10px" }}>
            Cancelar edición
          </button>
        )}
      </form>

      {mensaje && <p>{mensaje}</p>}

      <h2>Registros Capturados</h2>

      <table border="1" cellPadding="10" cellSpacing="0" width="100%">
        <thead>
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Email</th>
            <th>Asunto</th>
            <th>Mensaje</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {contacts.length > 0 ? (
            contacts.map((contact) => (
              <tr key={contact.id}>
                <td>{contact.id}</td>
                <td>{contact.name}</td>
                <td>{contact.email}</td>
                <td>{contact.subject}</td>
                <td>{contact.message}</td>
                <td>
                  <button onClick={() => handleEdit(contact)}>Editar</button>
                  <button
                    onClick={() => handleDelete(contact.id)}
                    style={{ marginLeft: "10px" }}
                  >
                    Eliminar
                  </button>
                </td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="6">No hay registros</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default App;