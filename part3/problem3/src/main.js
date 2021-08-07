// main.js ---------------------------------------------------------------------
import { App } from "/app.js";

function setup() {
  mount(App, { target: document.body });
}

owl.utils.whenReady(setup);