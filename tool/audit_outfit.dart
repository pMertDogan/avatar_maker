// Renders the bare body silhouette plus every outfit composited on the same
// canvas (nothing else selected), so a pixel analysis can measure (a) how far
// an outfit spills past the body and (b) what skin gaps it leaves at the neck
// and chest.
//
// Run: flutter test tool/audit_outfit.dart
// Outputs:
//   build/outfit/body.png          the body silhouette alone
//   build/outfit/item/<Name>.png   <Name> composited onto the bare body
import 'dart:io';
import 'dart:ui' as ui;

import 'package:avatar_maker/avatar_maker.dart';
import 'package:avatar_maker/src/core/services/avatar_service.dart';
import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:flutter_test/flutter_test.dart';

const _w = 264;
const _h = 280;

String _avatar(String outfit) => AvatarService.drawSVG(
      backgroundStyle: '',
      outfit: outfit,
      facialHair: '',
      mouth: '',
      nose: '',
      eyes: '',
      eyebrows: '',
      accessory: '',
      hair: '',
      skin: '',
    );

Future<void> _write(String path, String svg) async {
  final info = await vg.loadPicture(SvgStringLoader(svg), null);
  final recorder = ui.PictureRecorder();
  final canvas = Canvas(recorder);
  canvas.drawPicture(info.picture);
  final picture = recorder.endRecording();
  final image = await picture.toImage(_w, _h);
  final bytes = await image.toByteData(format: ui.ImageByteFormat.png);
  File(path).writeAsBytesSync(bytes!.buffer.asUint8List());
  info.picture.dispose();
  image.dispose();
  picture.dispose();
}

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  test('render body and each outfit alone', () async {
    Directory('build/outfit/item').createSync(recursive: true);
    await _write('build/outfit/body.png', _avatar(''));

    final probe = NonPersistentAvatarMakerController();
    for (final category in probe.propertyCategories) {
      if (category.id.name != 'OutfitType') continue;
      final items = category.properties!;
      for (final item in items) {
        final name = item.id.split('/').last;
        final raw = item.value
            .trim()
            .replaceAll(r'$TO_REPLACE_WITH_OUTFIT_COLOR', '#3366CC')
            .replaceAll(r'$TO_REPLACE_WITH_OUTFIT_COLOR_NAME', 'Color');
        if (raw.isEmpty) continue;
        await _write('build/outfit/item/$name.png', _avatar(raw));
      }
    }
  });
}
