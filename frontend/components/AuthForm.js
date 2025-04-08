export default function AuthForm({ type }) {
    return (
      <form>
        <h2>{type === 'login' ? 'Login' : 'Register'}</h2>
        <input type="text" placeholder="Username" /><br />
        <input type="password" placeholder="Password" /><br />
        <button type="submit">{type === 'login' ? 'Login' : 'Register'}</button>
      </form>
    );
  }
  