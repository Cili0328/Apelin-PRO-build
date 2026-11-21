import json
from pathlib import Path
keys = ['API Format','Chat Completions','Choose an API format first.','Enter a model ID supported by this endpoint.','Enter a valid model ID without spaces or line breaks.','Responses API','Testing Connection','The model responded successfully.','The sign-in ended during the connection test. Start again to continue.','Verifying the model with this endpoint…']
values = {
'ar': ['تنسيق API','Chat Completions','اختر تنسيق API أولاً.','أدخل معرّف نموذج تدعمه نقطة النهاية هذه.','أدخل معرّف نموذج صالحًا دون مسافات أو فواصل أسطر.','Responses API','جارٍ اختبار الاتصال','استجاب النموذج بنجاح.','انتهى تسجيل الدخول أثناء اختبار الاتصال. ابدأ من جديد للمتابعة.','جارٍ التحقق من النموذج باستخدام نقطة النهاية هذه…'],
'de': ['API-Format','Chat Completions','Wähle zuerst ein API-Format.','Gib eine von diesem Endpunkt unterstützte Modell-ID ein.','Gib eine gültige Modell-ID ohne Leerzeichen oder Zeilenumbrüche ein.','Responses API','Verbindung wird getestet','Das Modell hat erfolgreich geantwortet.','Die Anmeldung wurde während des Verbindungstests beendet. Starte sie erneut, um fortzufahren.','Modell wird mit diesem Endpunkt überprüft…'],
'es': ['Formato de API','Chat Completions','Elige primero un formato de API.','Introduce un ID de modelo compatible con este endpoint.','Introduce un ID de modelo válido sin espacios ni saltos de línea.','Responses API','Probando conexión','El modelo respondió correctamente.','El inicio de sesión terminó durante la prueba de conexión. Vuelve a empezar para continuar.','Verificando el modelo con este endpoint…'],
'fr': ['Format d’API','Chat Completions','Choisissez d’abord un format d’API.','Saisissez un identifiant de modèle pris en charge par ce point de terminaison.','Saisissez un identifiant de modèle valide sans espaces ni sauts de ligne.','Responses API','Test de la connexion','Le modèle a répondu correctement.','La connexion au compte s’est terminée pendant le test. Recommencez pour continuer.','Vérification du modèle avec ce point de terminaison…'],
'it': ['Formato API','Chat Completions','Scegli prima un formato API.','Inserisci un ID modello supportato da questo endpoint.','Inserisci un ID modello valido senza spazi o interruzioni di riga.','Responses API','Verifica della connessione','Il modello ha risposto correttamente.','L’accesso è terminato durante il test della connessione. Ricomincia per continuare.','Verifica del modello con questo endpoint…'],
'ja': ['API 形式','Chat Completions','最初に API 形式を選択してください。','このエンドポイントが対応するモデル ID を入力してください。','空白や改行を含まない有効なモデル ID を入力してください。','Responses API','接続をテスト中','モデルが正常に応答しました。','接続テスト中にサインインが終了しました。続行するには最初からやり直してください。','このエンドポイントでモデルを検証中…'],
'ko': ['API 형식','Chat Completions','먼저 API 형식을 선택하세요.','이 엔드포인트에서 지원하는 모델 ID를 입력하세요.','공백이나 줄바꿈이 없는 유효한 모델 ID를 입력하세요.','Responses API','연결 테스트 중','모델이 정상적으로 응답했습니다.','연결 테스트 중에 로그인이 종료되었습니다. 계속하려면 다시 시작하세요.','이 엔드포인트로 모델을 확인하는 중…'],
'pt-BR': ['Formato da API','Chat Completions','Escolha primeiro um formato de API.','Insira um ID de modelo compatível com este endpoint.','Insira um ID de modelo válido sem espaços ou quebras de linha.','Responses API','Testando conexão','O modelo respondeu com sucesso.','O login terminou durante o teste de conexão. Comece novamente para continuar.','Verificando o modelo com este endpoint…'],
'ru': ['Формат API','Chat Completions','Сначала выберите формат API.','Введите ID модели, поддерживаемой этой конечной точкой.','Введите корректный ID модели без пробелов и переносов строк.','Responses API','Проверка подключения','Модель успешно ответила.','Вход завершился во время проверки подключения. Начните заново, чтобы продолжить.','Проверка модели через эту конечную точку…'],
'vi': ['Định dạng API','Chat Completions','Hãy chọn định dạng API trước.','Nhập ID mô hình được điểm cuối này hỗ trợ.','Nhập ID mô hình hợp lệ, không có dấu cách hoặc ký tự xuống dòng.','Responses API','Đang kiểm tra kết nối','Mô hình đã phản hồi thành công.','Quá trình đăng nhập đã kết thúc trong khi kiểm tra kết nối. Hãy bắt đầu lại để tiếp tục.','Đang xác minh mô hình với điểm cuối này…'],
'zh-Hant': ['API 格式','Chat Completions','請先選擇 API 格式。','輸入此端點支援的模型 ID。','輸入有效的模型 ID，且不要包含空格或換行。','Responses API','正在測試連線','模型回應正常。','連線測試期間登入流程已結束。請重新開始。','正在透過此端點驗證模型…']
}
p=Path('source/Apelin-fixed/Apelin/Resources/Localizable.xcstrings')
catalog=json.loads(p.read_text())
for locale, translations in values.items():
    assert len(translations)==len(keys)
    for key,value in zip(keys,translations):
        catalog['strings'][key]['localizations'][locale]={'stringUnit':{'state':'translated','value':value}}
p.write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
print('Added 110 missing localized values.')

session = Path('source/Apelin-fixed/Packages/ApelinAgent/Sources/ApelinAgent/Session/AgentSession.swift')
text = session.read_text()
auto = '            autoCompact: Self.automaticCompactionOptions(for: resolved.model, journal: journal),\n'
assert text.count(auto) == 1
text = text.replace(auto, '')
anchor = '            authResolver: resolved.authResolver,\n'
assert text.count(anchor) == 1
text = text.replace(anchor, auto + anchor)
session.write_text(text)
print('Ordered betweenTurns before autoCompact to match pinned AgentOptions initializer.')

verification = Path('source/Apelin-fixed/Packages/ApelinAgent/Tests/ApelinAgentWorkerTests/ProviderKeyVerificationTests.swift')
text = verification.read_text()
assert text.count('try await makeServer(') == 4
verification.write_text(text.replace('try await makeServer(', 'try await Self.makeServer('))
print('Qualified four static verification server calls.')

source_root = Path('source/Apelin-fixed')
def patch_source(relative, before, after):
    path = source_root / relative
    content = path.read_text()
    assert content.count(before) == 1, (relative, before)
    path.write_text(content.replace(before, after))

patch_source('Packages/ApelinAgent/Tests/ApelinAgentTests/LongLogTests.swift',
    '#expect(seq == UInt64(lines) + 1, "the abandoned approval is closed")',
    '#expect(seq == UInt64(lines) + 2, "the abandoned approval is closed and the model window is recorded")')
patch_source('Packages/ApelinAgent/Tests/ApelinAgentTests/LongLogTests.swift',
    '#expect(await reopened.log.lastSeq == seq + 1)',
    '#expect(await reopened.log.lastSeq == seq + 2)')
patch_source('Packages/ApelinAgent/Tests/ApelinAgentTests/ScriptedSessionTests.swift',
    '#expect(events.first == .promptSubmitted(text: "Turn the hook on, build, install and check it loaded."))',
    '#expect(events.first == .contextWindow(128_000))\n        #expect(events.dropFirst().first == .promptSubmitted(text: "Turn the hook on, build, install and check it loaded."))')
patch_source('Packages/ApelinAgent/Tests/ApelinAgentWorkerTests/AccountDeskTests.swift',
    'try await response.value\n        #expect(try await store.credentials(for: CredentialProviderID.openAICompatible) == candidate)',
    'try await response.value\n        try await recorder.waitFor { $0.state != nil }\n        #expect(recorder.state == .succeeded)\n        #expect(try await store.credentials(for: CredentialProviderID.openAICompatible) == candidate)')
patch_source('Packages/ApelinAgent/Tests/ApelinAgentTests/CompactionTests.swift',
    'func `overflow retries from existing user turn without duplicating prompt`() async throws {',
    'func `SDK compaction failure retries from existing user turn without duplicating prompt`() async throws {')
patch_source('Packages/ApelinAgent/Tests/ApelinAgentTests/CompactionTests.swift',
    'var refused = fauxAssistantMessage(blocks: [], stopReason: .error, errorMessage: "maximum context length exceeded")\n        refused.failure = ProviderFailure(message: "maximum context length exceeded", httpStatus: 400)\n        faux.setResponses([\n',
    '// Emulate the terminal SDK error after its own compaction has failed.\n        // A raw provider overflow would first consume another faux reply as a recap.\n        let refused = fauxAssistantMessage(blocks: [], stopReason: .error, errorMessage:\n            "context is too large and compaction failed: compaction left 120801 tokens, above the recovery target of 78643")\n        faux.setResponses([\n')
print('Updated window-event assertions, awaited credential persistence, and isolated terminal SDK overflow recovery.')

patch_source('Apelin/Interface/Settings/Accounts/ProviderBalanceScreen.swift',
    r'return "\(formatter.string(from: NSNumber(value: amount)) ?? \"\(amount)\") quota"',
    'let number = formatter.string(from: NSNumber(value: amount)) ?? String(amount)\n            return "\\(number) quota"')
print('Fixed quota amount interpolation syntax.')

makefile = source_root / 'Makefile'
text = makefile.read_text()
assert text.count('swift test --package-path') == 2
makefile.write_text(text.replace('swift test --package-path', 'swift test --no-parallel --package-path'))
print('Run regression tests serially on hosted runners; timeout assertions stay unchanged.')
