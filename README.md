# QR Code Generator 🎨

A beautiful, modern QR code generator with a sleek gradient UI, real-time validation, and advanced customization options.

## ✨ Features

- **Beautiful Modern UI**: Stunning gradient design with smooth animations and transitions
- **Real-time Character Counter**: Instantly see how many characters you've entered
- **Smart Version Detection**: Automatic calculation of minimum required QR code version
- **Error Correction Levels**: Support for all four levels (L, M, Q, H) with detailed capacity information
- **Custom Colors**: Pick any color for your QR code using the color picker
- **Auto-scaling Display**: QR codes displayed at 300% for better visibility
- **Inline Error Messages**: Clear, non-intrusive error feedback without popups
- **Responsive Capacity Table**: Interactive table showing character limits for each version and error level
- **Auto Version Adjustment**: Automatically increases version if the specified one is too low

## 🚀 Quick Start

1. Open `JS.html` in any modern web browser
2. Enter your text in the large input field (up to 800px wide)
3. Select an error correction level
4. (Optional) Specify a QR code version (1-40)
5. (Optional) Choose a custom color
6. Click "Generate QR Code"

## 📊 Error Correction Levels

| Level | Recovery Capability | Use Case |
|-------|-------------------|----------|
| **L** | ~7% | Clean environments, maximum data capacity |
| **M** | ~15% | General use (recommended) |
| **Q** | ~25% | Outdoor use, potential damage |
| **H** | ~30% | Industrial, harsh environments |

Higher error correction = more reliable but lower data capacity.

## 🎯 QR Code Versions

- **Version 1-7**: Displayed in the capacity reference table
- **Versions 1-40**: All supported by the generator
- **Module Size**: Each version increases by 4 modules (Version 1 = 21×21, Version 2 = 25×25, etc.)

The app automatically recommends the minimum version needed based on your text length and selected error correction level.

## 💡 Interface Features

### Input Controls
- **800px wide text input** for comfortable typing
- **Color picker** for QR code customization
- **Version selector** with range 1-40
- **Error correction dropdown** with clear descriptions

### Real-time Feedback
- **Character count** updates as you type
- **Minimum version needed** calculated dynamically
- **Error messages** displayed inline (no annoying popups)
- **Final version used** shown after generation

### Visual Design
- Gradient purple/blue background
- Clean white input fields with hover effects
- Semi-transparent info displays with backdrop blur
- Smooth transitions and animations
- 300% scaled QR code display with white background

## 🛠️ Technical Details

- **Library**: [qrcode-generator](https://github.com/kazuhikoarase/qrcode-generator) by Kazuhiko Arase
- **Technology**: Pure HTML5, CSS3, and Vanilla JavaScript
- **No Build Process**: Single standalone HTML file
- **CDN Delivery**: Minimal load time, always up-to-date library

## 🌐 Browser Compatibility

Compatible with all modern browsers supporting:
- HTML5 Canvas API
- CSS3 Transforms and Gradients
- ES6 JavaScript
- HTML5 Color Input

Tested on: Chrome, Firefox, Safari, Edge

## 📝 Notes

- QR codes are generated client-side (your data never leaves your browser)
- The capacity table shows character limits for alphanumeric encoding
- Actual capacity may vary based on data type (numeric, alphanumeric, binary, kanji)
- Higher versions create larger, more complex QR codes

## 🎨 Customization

The interface uses a beautiful gradient color scheme that can be easily customized in the CSS section:
- Background: Purple to blue gradient (`#667eea` to `#764ba2`)
- Button: Pink to red gradient (`#f093fb` to `#f5576c`)
- All colors are easily modifiable in the `<style>` section

---

**Enjoy creating beautiful QR codes!** 💜
