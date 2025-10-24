# AR Greeting Card Project

## 🎉 Interactive AR Birthday Greeting Card

This project creates an immersive Augmented Reality greeting card experience using WebXR and AR.js technologies.

## Features

### 🎨 Visual Elements
- **3D Greeting Card**: Animated rotating card base
- **Floating Hearts**: Multiple colored hearts with smooth animations
- **3D Birthday Cake**: Rotating cake with animated flame
- **Colorful Balloons**: Floating balloons in different colors
- **Gift Box**: Rotating present with ribbon
- **Confetti**: Animated celebration particles
- **Interactive Message**: "Happy Birthday!" text with color animation

### 🎮 Interactive Features
- **Click Interaction**: Tap anywhere to create confetti explosion
- **Sound Effects**: Audio feedback on interaction
- **Smooth Animations**: All elements have fluid motion
- **Responsive Design**: Works on mobile and desktop

### 📱 AR Technology
- **AR.js Integration**: Marker-based AR tracking
- **WebXR Support**: Cross-platform AR experience
- **Camera Integration**: Real-time camera feed
- **Marker Detection**: Custom AR marker pattern

## Files

1. **`ar-greeting-card.html`** - Main AR greeting card application
2. **`ar-marker.html`** - Printable AR marker for tracking

## How to Use

### Step 1: Print the Marker
1. Open `ar-marker.html` in your browser
2. Click "Print This Marker" button
3. Print on white paper
4. Cut out the marker along the border

### Step 2: Experience the AR Card
1. Open `ar-greeting-card.html` in your mobile browser
2. Allow camera permissions when prompted
3. Point your camera at the printed marker
4. Watch the magical AR greeting unfold!
5. Tap anywhere on screen for confetti explosion

## Technical Requirements

- **Modern Browser**: Chrome, Firefox, Safari (mobile recommended)
- **Camera Access**: Required for AR functionality
- **Internet Connection**: For loading AR.js libraries
- **HTTPS**: Required for camera access (use local server for development)

## Browser Compatibility

- ✅ Chrome (Android/iOS)
- ✅ Firefox (Android/iOS)
- ✅ Safari (iOS)
- ✅ Edge (Windows/Android)
- ⚠️ Desktop browsers (limited AR support)

## Customization

### Change Colors
Edit the `color` attributes in the HTML:
```html
<a-sphere color="#FF69B4">  <!-- Pink heart -->
<a-box color="#FFD700">     <!-- Gold element -->
```

### Modify Animations
Adjust animation properties:
```html
animation="property: rotation; to: 0 360 0; loop: true; dur: 10000"
```

### Add New Elements
Create new 3D objects within the `<a-marker>` tags:
```html
<a-sphere position="0 1 0" radius="0.1" color="#FF0000"></a-sphere>
```

## Troubleshooting

### Camera Not Working
- Ensure HTTPS connection
- Check browser permissions
- Try refreshing the page
- Use mobile device for best experience

### Marker Not Detecting
- Ensure good lighting
- Keep marker flat and stable
- Move camera slowly
- Check marker is fully visible

### Performance Issues
- Close other browser tabs
- Use modern device
- Ensure stable internet connection

## Development

### Local Server Setup
```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx http-server

# Using PHP
php -S localhost:8000
```

### Testing
1. Start local server
2. Open `ar-greeting-card.html` in browser
3. Print marker from `ar-marker.html`
4. Test AR functionality

## Future Enhancements

- [ ] Multiple greeting themes
- [ ] Voice messages
- [ ] Social sharing
- [ ] Custom 3D models
- [ ] Multi-marker support
- [ ] Hand tracking
- [ ] Face filters

## License

This project is open source and available under the MIT License.

---

**Enjoy your AR greeting card experience! 🎉**
