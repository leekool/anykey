<div class="border position-centre">
    <div class="main ">
        <div class="navbar main-item">
            <div class="navbar-text">layout_gen</div>
            <div class="navbar-buttons">
                <span class="ri-minimise">
                </span>
                <span class="ri-maximise">
                </span>
                <span class="ri-close">
                </span>
            </div>
        </div>
        <div class="content main-item">
            <!-- content -->
        </div>
    </div>
</div>

<style>
@import url("../../static/fonts/real-icons.css");

.main {
  display: flex;
  flex: 1 1 auto;
  padding: 5px 0px 0px 5px;
  flex-direction: column;
  font-family: 'Tamzen', sans-serif;
}

.main-item {
  position: sticky;
  width: calc(100% - 5px);
}

.border {
  display: flex;
  position: absolute;
  width: 100%;
  flex-direction: column;
  height: calc(100% - 30px); /* 30px to account for taskbar */
  box-shadow: 0 0 0 1px #494b46 inset,
              0 0 0 3px #686d62 inset,
              0 0 0 6px #494b46 inset,
              0 3px 15px rgba(0, 0, 0, 0.3);
}

.focus {
  box-shadow: 0 0 0 1px #222020 inset,
              0 0 0 3px #32302c inset,
              0 0 0 6px #222020 inset,
              0 3px 15px rgba(0, 0, 0, 0.3);
  z-index: 10;
}

.navbar {
  display: flex;
  height: 25px;
  color: #e4e3d5;
  justify-content: flex-end;
  background-repeat: repeat;
  background-image: url('src/assets/images/pixmaps/navbar-tile.png');
  box-shadow: 0 -1px 0 0 #5c6057 inset;
  user-select: none;
}

.navbar-text {
  display: flex;
  height: 28px;
  left: 50%;
  font-size: 15px;
  align-items: center;
  position: absolute;
  transform: translate(-50%);
}

.navbar-buttons {
  display: flex;
  max-width: 90px;
  align-items: center;
  justify-content: center;
  margin-right: 2px;
}

.navbar-buttons span {
  font-size: 8px;
  padding: 8px;
  cursor: pointer;
}

.navbar-buttons span:hover {
  opacity: 0.4;
}

.content {
  display: flex;
  flex: 1 1 auto;
  max-height: calc(100% - 29.5px);
}

.position-centre {
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  -ms-transform: translate(-50%, -52.5%);
  transform: translate(-50%, -52.5%);
  max-height: 80%;
  width: 80%;
  max-width: 1200px;
}
</style>
