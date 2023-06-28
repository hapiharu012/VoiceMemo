//
//  ContentView.swift
//  OnseiMemo
//
//  Created by k21123kk on 2023/01/7.
//

import SwiftUI

// APIから取得する戻り値の型
struct Response: Codable {
  var results: [Result]
}

// 個々の保存データの型
struct Result: Codable {
  var memo: String? //メモ内容
  var time: String? //メモした日時
}


struct ContentView: View {
  
  @State private var results = [Result]()   // 空のメモデータの配列を生成
  
  var body: some View {
    
    NavigationView {
      VStack{
        
        List(results, id: \.time) { item in
          
          VStack(alignment: .leading) {
            
            HStack{
              Text(item.memo ?? "").font(.body)
            }
            
            HStack{
              Image(systemName: "calendar.badge.clock").resizable().scaledToFit().frame(height: 15)
              Text("：")
              Text(item.time ?? "")
            }
            
          }
          
        }.navigationTitle("音声メモ")
        Button(action:loadData){
          Text("更新").font(.title3).foregroundColor(Color.black)
        }
        
      }
      
    }.onAppear(perform: loadData)           // データ読み込み処理(アプリが開かれた時)
    
  }
  
  
  
  // データ読み込み関数
  func loadData() {
    guard let url = URL(string: "http://10.1.53.179:2000/") else {
      //"http://●●●●:2000/"これの●●●●の部分に接続されているネットワークのIPアドレスを埋め込む
      return
    }
    
    
    // URLリクエストの生成
    let request = URLRequest(url: url)
    
    // URLにアクセス
    URLSession.shared.dataTask(with: request) { data, response, error in
      
      if let data = data {  // ①データ取得チェック
        // ②JSON→Responseオブジェクト変換
        let decoder = JSONDecoder()
        guard let decodedResponse = try? decoder.decode(Response.self, from: data) else {
          print("Json decode エラー")
          return
        }
        // ③
        DispatchQueue.main.async {
          results = decodedResponse.results
        }
      } else {
        // ④データが取得できなかった場合の処理
        print("Fetch failed: \(error?.localizedDescription ?? "Unknown error")")
      }
    }.resume()      // タスク開始処理（必須）
  }
}

struct ContentView_Previews: PreviewProvider {
  static var previews: some View {
    Group {
      ContentView()
    }
  }
}

