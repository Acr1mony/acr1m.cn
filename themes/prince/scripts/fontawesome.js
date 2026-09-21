'use strict';

const fs = require('fs');
const path = require('path');

const packageRoot = path.dirname(require.resolve('@fortawesome/fontawesome-free/package.json'));
const assetGroups = [
  { source: 'css', output: 'vendor/fontawesome/css' },
  { source: 'webfonts', output: 'vendor/fontawesome/webfonts' }
];

hexo.extend.generator.register('fontawesome-assets', function () {
  return assetGroups.flatMap(function (group) {
    const sourceDir = path.join(packageRoot, group.source);

    return fs.readdirSync(sourceDir).map(function (filename) {
      const source = path.join(sourceDir, filename);

      return {
        path: group.output + '/' + filename,
        data: function () {
          return fs.createReadStream(source);
        }
      };
    });
  });
});
