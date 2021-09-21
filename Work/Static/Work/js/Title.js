// external npm package: tsparticles-interaction-light
loadLightInteraction(tsParticles);

// tsParticles - https://particles.js.org
tsParticles.load("tsparticles", {
  fpsLimit: 60,
  particles: {
    number: {
      value: 20,
      density: {
        enable: false,
        area: 800
      }
    },
    color: {
      value: "#ff0000",
      animation: {
        enable: true,
        speed: 10,
        sync: true
      }
    },
    shape: {
      type: ["circle"]
    },
    opacity: {
      value: 0.8
    },
    size: {
      value: 20,
      random: {
        enable: true,
        minimumValue: 18
      }
    },
    rotate: {
      value: 1,
      direction: "clockwise",
      animation: {
        speed: 5,
        enable: true
      }
    },
    move: {
      enable: true,
      speed: 3,
      direction: "none",
      outModes: { default: "out" }
    }
  },
  interactivity: {
    detectsOn: "canvas",
    events: {
      onHover: {
        enable: true,
        mode: "light"
      },
      resize: true
    },
    modes: {
      light: {
        area: {
          gradient: {
            start: "3b5e98",
            stop: "#17163e"
          }
        },
        shadow: {
          color: "#17163e"
        }
      }
    }
  },
  detectRetina: true,
  background: {
    color: "#17163e"
  }
});
Splitting()
