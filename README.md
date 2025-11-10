# QR Code Generator

A simple, browser-based QR code generator with customizable error correction levels, versions, and colors.

## Features

- **Dynamic QR Code Generation**: Generate QR codes from any text input
- **Error Correction Levels**: Support for all four error correction levels (L, M, Q, H)
- **Version Control**: Manually specify QR code versions (1-40) or auto-adjust based on text length
- **Color Customization**: Choose custom colors for your QR codes
- **Real-time Feedback**: 
  - Character counter
  - Minimum version recommendation
  - Capacity information table
- **Automatic Version Adjustment**: Automatically increases version if specified version is too low

## Usage

1. Open `JS.html` in any modern web browser
2. Enter the text you want to encode in the input field
3. Select an error correction level:
   - **L (7%)**: Low error correction
   - **M (15%)**: Medium error correction
   - **Q (25%)**: Quartile error correction
   - **H (30%)**: High error correction
4. (Optional) Specify a QR code version (1-40)
5. (Optional) Choose a color using the color picker
6. Click "Generate QR Code"

## Error Correction Levels

| Level | Error Correction Capability | Character Capacity |
|-------|----------------------------|-------------------|
| L | ~7% | Highest |
| M | ~15% | High |
| Q | ~25% | Medium |
| H | ~30% | Lowest |

## QR Code Versions

The application displays a capacity table for versions 1-7, showing:
- Maximum character capacity for each error correction level
- QR code size in modules

**Note**: The application supports all versions from 1 to 40. Higher versions can encode more data but result in larger, more complex QR codes.

## Technical Details

- **Library**: Uses [qrcode-generator](https://github.com/kazuhikoarase/qrcode-generator) via CDN
- **No Dependencies**: Standalone HTML file with embedded CSS and JavaScript
- **Offline Use**: Once loaded, can work offline (CDN required for initial load)

## Browser Compatibility

Works on all modern browsers that support:
- HTML5 Canvas
- ES6 JavaScript
- Color input type

## License

This is a simple demonstration project. Feel free to use and modify as needed.
