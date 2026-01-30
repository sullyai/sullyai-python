# Changelog

## 0.1.0-alpha.12 (2026-01-30)

Full Changelog: [v0.1.0-alpha.11...v0.1.0-alpha.12](https://github.com/sullyai/sullyai-python/compare/v0.1.0-alpha.11...v0.1.0-alpha.12)

### Features

* **api:** api update ([a1b5ba4](https://github.com/sullyai/sullyai-python/commit/a1b5ba49290ecb23e170baf36e849f1303c53f88))
* **client:** add custom JSON encoder for extended type support ([a83b8ba](https://github.com/sullyai/sullyai-python/commit/a83b8baf9540bb3cde5eb74c8c10ec57e1bb5919))
* **client:** add support for binary request streaming ([9b548a6](https://github.com/sullyai/sullyai-python/commit/9b548a6cf70396dc0450e55b6f149b3efb133f77))
* **client:** support file upload requests ([e959eb3](https://github.com/sullyai/sullyai-python/commit/e959eb38455e39814a6ad7374e526f741d8a2d48))
* improve future compat with pydantic v3 ([9d5a7d8](https://github.com/sullyai/sullyai-python/commit/9d5a7d87a61833b92b1f8ef412321e80a05851a3))
* **types:** replace List[str] with SequenceNotStr in params ([d8155f5](https://github.com/sullyai/sullyai-python/commit/d8155f5119bd4b504d1548a6a8f0e80c96441d1b))


### Bug Fixes

* avoid newer type syntax ([4b82db1](https://github.com/sullyai/sullyai-python/commit/4b82db1eae977b1a391da9ddc0a45858f5939ba4))
* **client:** close streams without requiring full consumption ([63fc5b2](https://github.com/sullyai/sullyai-python/commit/63fc5b2f651e38b805e41512743145d4545bf418))
* compat with Python 3.14 ([402027d](https://github.com/sullyai/sullyai-python/commit/402027d99463f22193ff1970241dda9de3755945))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([df2ab03](https://github.com/sullyai/sullyai-python/commit/df2ab030fb86550f0337e67505ec3873c11b82f8))
* ensure streams are always closed ([ee906b8](https://github.com/sullyai/sullyai-python/commit/ee906b8f5df8d1fb5da110bb04df25f2a9e15636))
* **parsing:** ignore empty metadata ([59033a8](https://github.com/sullyai/sullyai-python/commit/59033a8c89bbe868381bd0fb98631f9ff9b828c7))
* **parsing:** parse extra field types ([8b4e226](https://github.com/sullyai/sullyai-python/commit/8b4e226ed3e04dfac401fc89d2533a27603b1ceb))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([8043a89](https://github.com/sullyai/sullyai-python/commit/8043a8936921dd3160f2abba9631744215d3809b))
* use async_to_httpx_files in patch method ([e6cdd03](https://github.com/sullyai/sullyai-python/commit/e6cdd0310f4ea08c3a32eaea29a4ff625e9caf27))


### Chores

* add missing docstrings ([25d70e2](https://github.com/sullyai/sullyai-python/commit/25d70e23499d9e6b6bf0c65b724fe143b225215d))
* add Python 3.14 classifier and testing ([63fc80e](https://github.com/sullyai/sullyai-python/commit/63fc80ecc51dad5225d8f5ca8cc88bb775f5525d))
* bump `httpx-aiohttp` version to 0.1.9 ([321f6d6](https://github.com/sullyai/sullyai-python/commit/321f6d65c1be753599c8cc9f769289f022da0682))
* **ci:** upgrade `actions/github-script` ([ee1117f](https://github.com/sullyai/sullyai-python/commit/ee1117f7376641adf5a65aebb5b21f498406fd2c))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([b91a8be](https://github.com/sullyai/sullyai-python/commit/b91a8be8786ba02f04b1a39a9afc620a833daf82))
* do not install brew dependencies in ./scripts/bootstrap by default ([5335fa4](https://github.com/sullyai/sullyai-python/commit/5335fa458a250cfe1dce644b8a00af14141f6d36))
* **docs:** use environment variables for authentication in code snippets ([61bdce4](https://github.com/sullyai/sullyai-python/commit/61bdce4d608f3b8a47e25464ff2c12b0b4945763))
* **internal/tests:** avoid race condition with implicit client cleanup ([9de2201](https://github.com/sullyai/sullyai-python/commit/9de2201aee00e3f9e705c380d7dc731fabc9677e))
* **internal:** add `--fix` argument to lint script ([d6e1a5a](https://github.com/sullyai/sullyai-python/commit/d6e1a5a9615de1f36f72435cf907db660d369934))
* **internal:** add missing files argument to base client ([7c87f94](https://github.com/sullyai/sullyai-python/commit/7c87f940faf32dcfed4b8515c1f0556982eb5da3))
* **internal:** add Sequence related utils ([78f6a89](https://github.com/sullyai/sullyai-python/commit/78f6a8990ee7f0c80c78d1cb751ff6dfae57f927))
* **internal:** change ci workflow machines ([99053fb](https://github.com/sullyai/sullyai-python/commit/99053fb68f9dd26c15c140d7506610c59a835b17))
* **internal:** codegen related update ([cbb9b67](https://github.com/sullyai/sullyai-python/commit/cbb9b678f24c76616785e9993c5876f24774a1f2))
* **internal:** codegen related update ([d623a27](https://github.com/sullyai/sullyai-python/commit/d623a272535f63c520410c31e9a610261d094a0f))
* **internal:** codegen related update ([fe00231](https://github.com/sullyai/sullyai-python/commit/fe00231393e3d4369d47c473baacd53174846f8a))
* **internal:** codegen related update ([298757c](https://github.com/sullyai/sullyai-python/commit/298757cc306c30ac685394004b6cf796a3bbceca))
* **internal:** detect missing future annotations with ruff ([1fead4e](https://github.com/sullyai/sullyai-python/commit/1fead4eadbf3457047e576ef32886e6d4101ec8b))
* **internal:** fix ruff target version ([1a6537f](https://github.com/sullyai/sullyai-python/commit/1a6537f645c0793bd528d1912af3c94414f888b9))
* **internal:** grammar fix (it's -&gt; its) ([c63d6c8](https://github.com/sullyai/sullyai-python/commit/c63d6c895f4867e47153374d425ec157e637a2ec))
* **internal:** move mypy configurations to `pyproject.toml` file ([a168da6](https://github.com/sullyai/sullyai-python/commit/a168da6c54df680c430d00386e905d32250119d3))
* **internal:** update `actions/checkout` version ([a823127](https://github.com/sullyai/sullyai-python/commit/a823127f9c43aa3e486cbf20b5e0977e7ada0173))
* **internal:** update comment in script ([8977a6d](https://github.com/sullyai/sullyai-python/commit/8977a6daacfcee37b1865b2235ac0e81cd6ec9f0))
* **internal:** update pydantic dependency ([668fca1](https://github.com/sullyai/sullyai-python/commit/668fca16889a148d92b55d373275cf92b2ccd613))
* **internal:** update pyright exclude list ([f2f5a4c](https://github.com/sullyai/sullyai-python/commit/f2f5a4c91f3b32b9126d08be664379ed9dfc6b5a))
* **package:** drop Python 3.8 support ([d36fbe6](https://github.com/sullyai/sullyai-python/commit/d36fbe6929728b39b198a34c77b756bbcf2435f3))
* **project:** add settings file for vscode ([0bad91b](https://github.com/sullyai/sullyai-python/commit/0bad91bd013e50f0446676398e7a1fa2d8e5af2e))
* speedup initial import ([acf5739](https://github.com/sullyai/sullyai-python/commit/acf57393f238da2eda9e689a64c5ec8bee27b000))
* **types:** change optional parameter type from NotGiven to Omit ([350585c](https://github.com/sullyai/sullyai-python/commit/350585cccc36012f920fc9aacc2620b5d538f073))
* **types:** rebuild Pydantic models after all types are defined ([34c6d30](https://github.com/sullyai/sullyai-python/commit/34c6d300c0696c125ed1eec3f7e001f52b918695))
* update @stainless-api/prism-cli to v5.15.0 ([c72e48f](https://github.com/sullyai/sullyai-python/commit/c72e48fe5c2ea46870718c0c86afffaa084c6185))
* update github action ([fbb9ef7](https://github.com/sullyai/sullyai-python/commit/fbb9ef7669726c8ee50799710b6ffb4a657be588))
* update lockfile ([6ca5340](https://github.com/sullyai/sullyai-python/commit/6ca534029bf6bea39e2d85d0f5ade00a7665f629))

## 0.1.0-alpha.11 (2025-07-15)

Full Changelog: [v0.1.0-alpha.10...v0.1.0-alpha.11](https://github.com/sullyai/sullyai-python/compare/v0.1.0-alpha.10...v0.1.0-alpha.11)

### Bug Fixes

* **client:** don't send Content-Type header on GET requests ([f3482ae](https://github.com/sullyai/sullyai-python/commit/f3482ae50b9ada914bef67cf30a1f9935ebe8d28))
* **parsing:** correctly handle nested discriminated unions ([9ee4101](https://github.com/sullyai/sullyai-python/commit/9ee410105d81f0f4eb142486d41013a6dc12b75f))


### Chores

* **ci:** change upload type ([70e2568](https://github.com/sullyai/sullyai-python/commit/70e2568ac8bfa37dab0c936aacf61494f5950378))
* **internal:** bump pinned h11 dep ([6b3d904](https://github.com/sullyai/sullyai-python/commit/6b3d90412382e5801da1a07e87cc97789601e679))
* **internal:** codegen related update ([2749b0e](https://github.com/sullyai/sullyai-python/commit/2749b0e54545d9e56361239962d1ada407e08124))
* **package:** mark python 3.13 as supported ([1471f9b](https://github.com/sullyai/sullyai-python/commit/1471f9b03ab5733e00dabaf7d730c90c834755d8))
* **readme:** fix version rendering on pypi ([513c235](https://github.com/sullyai/sullyai-python/commit/513c235fa5fd7af443ad75bc1dc8229a92c2cc9a))

## 0.1.0-alpha.10 (2025-06-30)

Full Changelog: [v0.1.0-alpha.9...v0.1.0-alpha.10](https://github.com/sullyai/sullyai-python/compare/v0.1.0-alpha.9...v0.1.0-alpha.10)

### Features

* **api:** api update ([d2fc1a2](https://github.com/sullyai/sullyai-python/commit/d2fc1a2318b474e59bfdecb32a38da67bc67af71))
* **client:** add support for aiohttp ([9d10831](https://github.com/sullyai/sullyai-python/commit/9d108315ee49f8c294f8a3cf1873173533aff61f))


### Bug Fixes

* **ci:** correct conditional ([2ff62e4](https://github.com/sullyai/sullyai-python/commit/2ff62e4c4d0ed172ec33d1b9c68eb0a5f00566cd))
* **ci:** release-doctor — report correct token name ([e184c1a](https://github.com/sullyai/sullyai-python/commit/e184c1a717647284be506768306702b61acfc2df))
* **client:** correctly parse binary response | stream ([aa58fe0](https://github.com/sullyai/sullyai-python/commit/aa58fe010963b67a6a61fbd7969c2d7e1c04256b))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([1f655ab](https://github.com/sullyai/sullyai-python/commit/1f655ab4a42b1d4fcb3d19e36abfb08f676ea9a5))


### Chores

* **ci:** enable for pull requests ([571f35c](https://github.com/sullyai/sullyai-python/commit/571f35c2da8296dd7656aaa1875497195798ec0f))
* **ci:** only run for pushes and fork pull requests ([e21efba](https://github.com/sullyai/sullyai-python/commit/e21efba5b3288773e4faf67b2389cb10c269ffdf))
* **internal:** update conftest.py ([ab70263](https://github.com/sullyai/sullyai-python/commit/ab70263395bf39559bf6559e55395cb93db3f39b))
* **readme:** update badges ([9e35244](https://github.com/sullyai/sullyai-python/commit/9e3524481bb9a31afbbed51cc8dd7afa5bebd480))
* **tests:** add tests for httpx client instantiation & proxies ([57c7d56](https://github.com/sullyai/sullyai-python/commit/57c7d56e0e6af93add9a774d66ffbafb462cc998))
* **tests:** run tests in parallel ([9546588](https://github.com/sullyai/sullyai-python/commit/95465889cc3bf6215ca2cc056bc57326dc66471a))
* **tests:** skip some failing tests on the latest python versions ([ae75e81](https://github.com/sullyai/sullyai-python/commit/ae75e818ff66f17854e8a2dfcb0d19464d809813))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([a9d1182](https://github.com/sullyai/sullyai-python/commit/a9d11825d69c705c17f492fd56c5635596305914))

## 0.1.0-alpha.9 (2025-06-03)

Full Changelog: [v0.1.0-alpha.8...v0.1.0-alpha.9](https://github.com/sullyai/sullyai-python/compare/v0.1.0-alpha.8...v0.1.0-alpha.9)

### Bug Fixes

* **package:** support direct resource imports ([6c3dade](https://github.com/sullyai/sullyai-python/commit/6c3dadec90580ad7d9a3756a85ed6b3f87f66acd))


### Chores

* **ci:** fix installation instructions ([e1cc82b](https://github.com/sullyai/sullyai-python/commit/e1cc82b1d638c5a401dd8667b062fd6a7d1d12f9))
* **ci:** upload sdks to package manager ([3f1f0cc](https://github.com/sullyai/sullyai-python/commit/3f1f0ccccfbe3fea63451de7ed1181d5284014b3))
* **docs:** grammar improvements ([b412bb6](https://github.com/sullyai/sullyai-python/commit/b412bb642de28f72bfc14a390d5cb382fe2591fe))
* **docs:** remove reference to rye shell ([fafb9d0](https://github.com/sullyai/sullyai-python/commit/fafb9d0e7d91b6634fc5f21153c74abf9157b9a8))
* **docs:** remove unnecessary param examples ([a9b5eca](https://github.com/sullyai/sullyai-python/commit/a9b5eca7cfd0af9e0b14d152b8c012c8deff00fc))
* **internal:** codegen related update ([e673cb3](https://github.com/sullyai/sullyai-python/commit/e673cb3657cbe818073d9800067d0e3db7fd46d0))

## 0.1.0-alpha.8 (2025-05-09)

Full Changelog: [v0.1.0-alpha.7...v0.1.0-alpha.8](https://github.com/sullyai/sullyai-python/compare/v0.1.0-alpha.7...v0.1.0-alpha.8)

### Features

* **api:** api update ([691dd06](https://github.com/sullyai/sullyai-python/commit/691dd06a42664388cbd7560595e07f5c2b8dc965))
* **api:** api update ([43f673e](https://github.com/sullyai/sullyai-python/commit/43f673e822cfb26d7b30dc37312ce7c5cb20c8ee))


### Chores

* **internal:** avoid errors for isinstance checks on proxies ([bbbe0e1](https://github.com/sullyai/sullyai-python/commit/bbbe0e1cd5ac93d1953a1051f89254f6f53dc299))

## 0.1.0-alpha.7 (2025-05-05)

Full Changelog: [v0.1.0-alpha.6...v0.1.0-alpha.7](https://github.com/sullyai/sullyai-python/compare/v0.1.0-alpha.6...v0.1.0-alpha.7)

### Features

* **api:** api update ([1c4cb2a](https://github.com/sullyai/sullyai-python/commit/1c4cb2a355cbbb18905e963974374de72e72c38e))

## 0.1.0-alpha.6 (2025-04-24)

Full Changelog: [v0.1.0-alpha.5...v0.1.0-alpha.6](https://github.com/sullyai/sullyai-python/compare/v0.1.0-alpha.5...v0.1.0-alpha.6)

### Bug Fixes

* **pydantic v1:** more robust ModelField.annotation check ([35b7fb9](https://github.com/sullyai/sullyai-python/commit/35b7fb9d7ccf668fd043ef1a9b26e67eaa314ef7))


### Chores

* broadly detect json family of content-type headers ([3477834](https://github.com/sullyai/sullyai-python/commit/34778348143b37d0937dad81c5d5043687cc98df))
* **ci:** add timeout thresholds for CI jobs ([e611549](https://github.com/sullyai/sullyai-python/commit/e6115494293145b19d6c08a26dbdbcd3a60f9c8e))
* **ci:** only use depot for staging repos ([38a5ab4](https://github.com/sullyai/sullyai-python/commit/38a5ab43196d5c4482f5990059e7a48d02f66040))
* **internal:** codegen related update ([3d5c7ea](https://github.com/sullyai/sullyai-python/commit/3d5c7ea34300a1b0fdc5caf1ae1e4acae6e6db7e))
* **internal:** fix list file params ([220314c](https://github.com/sullyai/sullyai-python/commit/220314c7708ccced412a9f3f6b44eca63bfc77b6))
* **internal:** import reformatting ([ee6c5f5](https://github.com/sullyai/sullyai-python/commit/ee6c5f540cfa2d1311c6ae5c422e4e900a420d6d))
* **internal:** refactor retries to not use recursion ([9d3f457](https://github.com/sullyai/sullyai-python/commit/9d3f457ca729d30315f44ea1ed5e1028c8cb5252))
* **internal:** update models test ([6d5f6ee](https://github.com/sullyai/sullyai-python/commit/6d5f6ee09f35343d00b9e45ef6c882fa4bb8395b))

## 0.1.0-alpha.5 (2025-04-17)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-alpha.5](https://github.com/sullyai/sullyai-python/compare/v0.1.0-alpha.4...v0.1.0-alpha.5)

### Features

* **api:** manual updates ([f79216b](https://github.com/sullyai/sullyai-python/commit/f79216bdd6008821b3999786b7981e628b60e443))

## 0.1.0-alpha.4 (2025-04-17)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/sullyai/sullyai-python/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Bug Fixes

* **client:** send all configured auth headers ([#20](https://github.com/sullyai/sullyai-python/issues/20)) ([dfba406](https://github.com/sullyai/sullyai-python/commit/dfba406bf81aab6de85671f7a43917bcf3f51a3a))
* **perf:** optimize some hot paths ([edfb8c1](https://github.com/sullyai/sullyai-python/commit/edfb8c1a69b0539b4a3a5fe10bea8f9528e579d6))
* **perf:** skip traversing types for NotGiven values ([7c65999](https://github.com/sullyai/sullyai-python/commit/7c65999995d97828971b73c1ec16f40df575af23))


### Chores

* **client:** minor internal fixes ([13c30ec](https://github.com/sullyai/sullyai-python/commit/13c30ec08268481f4185ef550e3f900f26ebe980))
* **internal:** base client updates ([0e838b2](https://github.com/sullyai/sullyai-python/commit/0e838b2193187b81ccf3e937dbe63a8f6595341f))
* **internal:** bump pyright version ([d9a1544](https://github.com/sullyai/sullyai-python/commit/d9a1544a1614f8c720322989e432119e2743ce42))
* **internal:** expand CI branch coverage ([9230e0b](https://github.com/sullyai/sullyai-python/commit/9230e0b69b429ffdaa501dc0631e5ca05c7e4150))
* **internal:** reduce CI branch coverage ([41c7753](https://github.com/sullyai/sullyai-python/commit/41c7753a24ae6cc6f427ab5a45bdf413d4535e05))
* **internal:** slight transform perf improvement ([#22](https://github.com/sullyai/sullyai-python/issues/22)) ([654e7a1](https://github.com/sullyai/sullyai-python/commit/654e7a1f26429787401ee17e42605ecdc96ea152))
* **internal:** update pyright settings ([710964f](https://github.com/sullyai/sullyai-python/commit/710964f01c5dc1acdbe3716737ad5c518a89cdf9))
* slight wording improvement in README ([#24](https://github.com/sullyai/sullyai-python/issues/24)) ([34fdf54](https://github.com/sullyai/sullyai-python/commit/34fdf545225208c6bcbd686f031b1e33cf6bd811))
* **tests:** improve enum examples ([#23](https://github.com/sullyai/sullyai-python/issues/23)) ([e6d8300](https://github.com/sullyai/sullyai-python/commit/e6d8300119ae8f9112f12c1ca59dc30a58fc9a48))


### Documentation

* remove private imports from datetime snippets ([11d21d1](https://github.com/sullyai/sullyai-python/commit/11d21d11679ca613ee3eacbb6ab63beb701992f2))

## 0.1.0-alpha.3 (2025-04-04)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/sullyai/sullyai-python/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Chores

* fix typos ([#17](https://github.com/sullyai/sullyai-python/issues/17)) ([a9501e3](https://github.com/sullyai/sullyai-python/commit/a9501e3d767d6c51a26e769c9e57f017d97712e9))
* **internal:** remove trailing character ([#19](https://github.com/sullyai/sullyai-python/issues/19)) ([9d2f872](https://github.com/sullyai/sullyai-python/commit/9d2f872f8651d30a26df4344b6864dab592c1558))

## 0.1.0-alpha.2 (2025-03-17)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/sullyai/sullyai-python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** manual updates ([#8](https://github.com/sullyai/sullyai-python/issues/8)) ([54f0497](https://github.com/sullyai/sullyai-python/commit/54f04979e0e876fe190fadfe68bb8cecd6237a72))


### Bug Fixes

* **ci:** ensure pip is always available ([#14](https://github.com/sullyai/sullyai-python/issues/14)) ([1ccc95c](https://github.com/sullyai/sullyai-python/commit/1ccc95cf1670b34f962f0b6958f767161d3fdcac))
* **ci:** remove publishing patch ([#15](https://github.com/sullyai/sullyai-python/issues/15)) ([588422e](https://github.com/sullyai/sullyai-python/commit/588422e4b4b9fc1aab561ea746aa7f33e72dbb1f))
* **internal:** fix auth logic with multiple auth methods ([87c827f](https://github.com/sullyai/sullyai-python/commit/87c827f116450eeb00d8403e63ebabcd9480aa84))
* **types:** handle more discriminated union shapes ([#13](https://github.com/sullyai/sullyai-python/issues/13)) ([600f99e](https://github.com/sullyai/sullyai-python/commit/600f99e19f925090e1c84a84b5924dbf042949a5))


### Chores

* **internal:** bump rye to 0.44.0 ([#12](https://github.com/sullyai/sullyai-python/issues/12)) ([c42f1af](https://github.com/sullyai/sullyai-python/commit/c42f1afce0777f34dcbafb05945f36f1a3c147b3))
* **internal:** codegen related update ([#11](https://github.com/sullyai/sullyai-python/issues/11)) ([a375b35](https://github.com/sullyai/sullyai-python/commit/a375b35378ff93d9fad2c10b15f4f95c82931f2e))
* **internal:** remove extra empty newlines ([#10](https://github.com/sullyai/sullyai-python/issues/10)) ([75b5335](https://github.com/sullyai/sullyai-python/commit/75b5335faab4995df79c5a210d7a6cb7dc0565c1))

## 0.1.0-alpha.1 (2025-03-11)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/sullyai/sullyai-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** api update ([#4](https://github.com/sullyai/sullyai-python/issues/4)) ([c17774d](https://github.com/sullyai/sullyai-python/commit/c17774da22f1390cf4abb6545b54d46c65565da8))
* **api:** api update ([#6](https://github.com/sullyai/sullyai-python/issues/6)) ([b1b23b0](https://github.com/sullyai/sullyai-python/commit/b1b23b061e778fa80846e7c2fb400c72c14f1b67))
* **api:** manual updates ([#5](https://github.com/sullyai/sullyai-python/issues/5)) ([1f43b70](https://github.com/sullyai/sullyai-python/commit/1f43b70f4900c587c41cf6baa2da5d77ae519062))


### Chores

* go live ([#1](https://github.com/sullyai/sullyai-python/issues/1)) ([0b58e83](https://github.com/sullyai/sullyai-python/commit/0b58e833a7d5d818b0f21d6c206c476affdb0056))
* update SDK settings ([#3](https://github.com/sullyai/sullyai-python/issues/3)) ([fbd61f1](https://github.com/sullyai/sullyai-python/commit/fbd61f12cb82075dab7772cf44e09b408c0b5ead))
