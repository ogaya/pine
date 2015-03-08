drop table statistics_result;
drop table correlation; 
drop table storage;
drop table target;
drop table tags;

-- 回帰分析のターゲット
create table target (
    -- タグ
    tag text,
    pattern_id integer[],
    PRiMARY KEY(tag)
);
-- 回帰分析の結果
create table statistics_result (
    -- 目的変数
    objective text,
    -- 目的変数のデータ時間
    obj_time timestamp,
    -- 説明変数
    explanatory text[],
    -- 説明変数のデータ時間
    exp_time timestamp[],
    -- 時間幅（秒換算）
    span int,
    -- 決定係数
    r_squared double precision,
    -- t値
    t double precision[],
    -- 係数
    coefficient double precision[],
    -- 重要変数（説明変数）
    --important text,
    -- その他詳細
    detail text,
    PRIMARY KEY(objective, obj_time, explanatory, exp_time, span)
);

-- 相関係数
create table correlation (
    x text,
    x_time timestamp,
    y text,
    y_time timestamp,
    val double precision,
    PRIMARY KEY(x, x_time, y, y_time)
);

-- 蓄積データ（テスト用）
create table storage (
    -- タグ
    tag text,
    -- タイムスタンプ
    timestamp timestamp,
    -- 値
    value double precision,
    PRIMARY KEY(tag,timestamp)
);

-- 全タグ集
create table tags(
    -- タグ
    tag text,
    PRIMARY KEY(tag)
);
