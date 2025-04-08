export default function Leaderboard({ leaderboard }) {
    return (
      <div>
        <h2>Leaderboard</h2>
        <ul>
          {leaderboard.map(([user, score]) => (
            <li key={user}>{user}: {score}</li>
          ))}
        </ul>
      </div>
    );
  }
  