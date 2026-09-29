const $ = id => document.getElementById(id);

const fields = {
  steps: { value: $("stepsValue"), stat: $("statSteps"), format: v => Number(v).toLocaleString() },
  exercise: { value: $("exerciseValue"), stat: $("statExercise"), format: v => `${v} min` },
  sleep: { value: $("sleepValue"), stat: $("statSleep"), format: v => `${v} hrs` },
  water: { value: $("waterValue"), stat: $("statWater"), format: v => `${Number(v).toFixed(1)} L` }
};

Object.keys(fields).forEach(key => {
  const input = $(key);
  input.addEventListener("input", () => {
    const v = input.value;
    fields[key].value.textContent = fields[key].format(v);
    fields[key].stat.textContent = fields[key].format(v);
    updatePreview();
  });
});

function calculateScore() {
  const steps = Number($("steps").value);
  const exercise = Number($("exercise").value);
  const sleep = Number($("sleep").value);
  const water = Number($("water").value);

  const stepScore = Math.min(steps / 10000, 1) * 35;
  const exerciseScore = Math.min(exercise / 45, 1) * 30;
  const sleepScore = Math.min(sleep / 8, 1) * 20;
  const waterScore = Math.min(water / 2.5, 1) * 15;
  return Math.round(stepScore + exerciseScore + sleepScore + waterScore);
}

function updatePreview() {
  const score = calculateScore();
  $("heroScore").textContent = score;
}

$("fitnessForm").addEventListener("submit", e => {
  e.preventDefault();
  const score = calculateScore();
  $("score").textContent = score;
  $("heroScore").textContent = score;
  $("progressBar").style.width = score + "%";
  $("score-ring");
  document.querySelector(".score-ring").style.background =
    `conic-gradient(var(--primary) ${score * 3.6}deg, #e9ebf2 ${score * 3.6}deg)`;

  let title, message;
  if (score >= 80) {
    title = "Great work! Your routine looks strong.";
    message = "Keep your activity consistent. Maintain good hydration and aim for a regular sleep schedule.";
  } else if (score >= 60) {
    title = "You're on the right track.";
    message = "Try adding a little more movement today and keep your water intake and sleep consistent.";
  } else {
    title = "Small steps can make a big difference.";
    message = "Start with a short walk, drink enough water, and work toward a regular sleep routine.";
  }

  $("scoreText").textContent = score >= 80 ? "Excellent daily activity." : score >= 60 ? "Good progress today." : "There is room to improve.";
  $("insightStatus").textContent = "Updated just now";
  $("insight").innerHTML = `
    <div class="spark">✦</div>
    <div><strong>${title}</strong><p>${message}</p></div>
  `;
});

$("themeBtn").addEventListener("click", () => {
  document.body.classList.toggle("dark");
  $("themeBtn").textContent = document.body.classList.contains("dark") ? "☀" : "☾";
});

updatePreview();
